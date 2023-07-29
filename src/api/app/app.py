"""
    Florgon API server application entry point.
    Provides FastAPI server.
    Should be run from external process (Manual uvicorn or by default as docker).
"""

from fastapi.logger import logger as fastapi_logger
from fastapi import FastAPI

from .routers import include_routers
from .middlewares import add_middlewares
from .exception_handlers import add_exception_handlers
from .event_handlers import add_event_handlers
from .database.bootstrap import wait_for_database_startup, create_start_database_entries
from .config import get_settings, get_logger
from . import database


def _cli_entry_point() -> None:
    """
    You are not supposed to run this directly.
    Raise error if tried to run from CLI directly.
    """
    print(
        "ERROR: This application should be run with `Uvicorn` manually, or by Docker (Docker-Compose).\n"
    )
    print(
        "ERROR: Please use methods above, or search FastAPI application inside `/app.py`"
    )
    exit(1)


def _construct_app() -> FastAPI:
    """
    Returns FastAPI application ready to run.
    Creates base FastAPI instance with registering all required stuff on it.
    """

    settings = get_settings()
    app_instance = FastAPI(
        debug=settings.fastapi_debug,
        # Custom settings.
        # By default, modified by setters (below), or empty if not used.
        routes=None,
        middleware=None,
        exception_handlers=None,
        dependencies=None,
        responses=None,
        callbacks=None,
        # Event handlers.
        on_shutdown=None,
        on_startup=None,
        # OpenAPI.
        title=settings.openapi_title,
        version=settings.openapi_version,
        description=settings.openapi_description,
        docs_url=settings.openapi_docs_url if settings.openapi_enabled else None,
        redoc_url=settings.openapi_redoc_url if settings.openapi_enabled else None,
        openapi_prefix=settings.openapi_prefix,
        openapi_url=settings.openapi_url if settings.openapi_enabled else None,
        openapi_tags=[
            # TODO!: Move or refactor that.
            {
                "name": "session",
                "description": "Session workflow methods, cannot be access by default user (direct-auth is allowed only for Florgon services)",
            },
            {
                "name": "user",
                "description": "Methods to get / edit user information or get other user information",
            },
            {
                "name": "utils",
                "description": "Some common utility methods like get status, get features, etc",
            },
            {
                "name": "security",
                "description": "Methods to work with user security information.",
            },
            {
                "name": "tokens",
                "description": "Methods to work with tokens mostly for external services",
            },
        ],
        # Other.
        root_path=settings.fastapi_root_path,
        root_path_in_servers=True,
    )

    # Register all internal stuff as routers/handlers/middlewares/database etc.
    add_event_handlers(app_instance)
    add_exception_handlers(app_instance)
    add_middlewares(app_instance)
    include_routers(app_instance)
    wait_for_database_startup()
    if settings.database_create_all:
        database.core.create_all()
        create_start_database_entries()

    # Logging.
    logger = get_logger()
    fastapi_logger.handlers = logger.handlers
    fastapi_logger.setLevel(logger.level)
    logger.info("[core] Hooked logging successfully!")

    return app_instance


if __name__ == "__main__":
    _cli_entry_point()

# Root application for uvicorn runner or whatever else.
# (Docker compose is running with app.app:app, means that this application instance
# will be served by uvicorn, and will be constructed at import).
app = _construct_app()
