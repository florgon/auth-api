"""
    FastAPI routers for application.
"""

from fastapi import FastAPI

from app.config import get_settings

from . import (
    utils,
    user,
    session,
    security,
    secure,
    oauth_client,
    oauth,
    mailings,
    gift,
    ext_oauth,
    email,
    admin,
)


def include_routers(app: FastAPI) -> None:
    """
    Registers (Including) FastAPI routers for FastAPI app.
    """
    proxy_url_prefix = get_settings().proxy_url_prefix
    for module in [
        oauth_client,
        email,
        session,
        oauth,
        user,
        utils,
        secure,
        ext_oauth,
        admin,
        security,
        gift,
        mailings,
    ]:
        app.include_router(module.router, prefix=proxy_url_prefix)
