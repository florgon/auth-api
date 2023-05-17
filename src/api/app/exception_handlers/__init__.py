"""
    Florgon server API exception handlers.
    (FastAPI exception handlers)
"""

from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI

from app.tokens.exceptions import (
    TokenWrongTypeError,
    TokenInvalidSignatureError,
    TokenInvalidError,
    TokenExpiredError,
)
from app.services.api.errors import ApiErrorException

from . import _handlers


def add_exception_handlers(app: FastAPI) -> None:
    """
    Adds exception handlers for application.
    """

    app.add_exception_handler(ApiErrorException, _handlers.api_error_exception_handler)
    app.add_exception_handler(
        RequestValidationError, _handlers.validation_exception_handler
    )

    app.add_exception_handler(TokenExpiredError, _handlers.token_expired_error_handler)
    app.add_exception_handler(
        TokenWrongTypeError, _handlers.token_wrong_type_error_handler
    )
    app.add_exception_handler(TokenInvalidError, _handlers.token_invalid_error_handler)
    app.add_exception_handler(
        TokenInvalidSignatureError, _handlers.token_invalid_signature_error_handler
    )

    app.add_exception_handler(404, _handlers.not_found_handler)
    app.add_exception_handler(405, _handlers.method_not_allowed)
    app.add_exception_handler(429, _handlers.too_many_requests_handler)
    app.add_exception_handler(500, _handlers.internal_server_error_handler)
