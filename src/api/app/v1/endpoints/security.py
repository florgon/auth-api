"""
    User security API router.
    Provides API methods (routes) for working with user security.
"""

from app.core.database.dependencies import Session, get_db
from app.core.services.api.response import ApiErrorCode, api_error, api_success
from app.core.services.permissions import Permission
from app.core.services.request import query_auth_data_from_request
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/security/info")
async def method_security_get_info(
    req: Request, db: Session = Depends(get_db)
) -> JSONResponse:
    """Returns security information about current user."""
    auth_data = query_auth_data_from_request(
        req, db, required_permissions=[Permission.security]
    )
    user = auth_data.user
    return api_success(
        {
            "security": {
                "tfa": {
                    "enabled": user.security_tfa_enabled,
                    "can_enabled": user.is_verified,
                    "device_type": "email",
                }
            }
        }
    )


@router.get("/security/tfa/enable")
async def method_security_user_enable_tfa(
    req: Request, db: Session = Depends(get_db)
) -> JSONResponse:
    """Enables TFA for the current user."""
    query_auth_data_from_request(req, db, required_permissions=[Permission.security])
    return api_error(
        ApiErrorCode.API_NOT_IMPLEMENTED,
        "Security not implemented yet (2FA not implemented).",
    )


@router.get("/security/tfa/disable")
async def method_security_user_disable_tfa(
    req: Request, db: Session = Depends(get_db)
) -> JSONResponse:
    """Disables TFA for the current user."""
    query_auth_data_from_request(req, db, required_permissions=[Permission.security])
    return api_error(
        ApiErrorCode.API_NOT_IMPLEMENTED,
        "Security not implemented yet (2FA not implemented).",
    )


@router.get("/security/password/change/request")
async def method_security_user_request_change_password(
    req: Request, db: Session = Depends(get_db)
) -> JSONResponse:
    """Requests change password for the current user."""
    query_auth_data_from_request(req, db, required_permissions=[Permission.security])
    return api_error(
        ApiErrorCode.API_NOT_IMPLEMENTED,
        "Security not implemented yet (Password change not implemented).",
    )


@router.get("/security/password/change/confirm")
async def method_security_user_confirm_change_password(
    req: Request, db: Session = Depends(get_db)
) -> JSONResponse:
    """Accepts change password for the current user."""
    query_auth_data_from_request(req, db, required_permissions=[Permission.security])
    return api_error(
        ApiErrorCode.API_NOT_IMPLEMENTED,
        "Security not implemented yet (Password change not implemented).",
    )
