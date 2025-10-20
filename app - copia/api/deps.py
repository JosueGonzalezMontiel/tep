from typing import Optional
from fastapi import HTTPException, Security, Request
from fastapi.security.api_key import APIKeyHeader, APIKeyQuery
from starlette.status import HTTP_401_UNAUTHORIZED
from app.core.config import API_KEY

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)
api_key_query = APIKeyQuery(name="api_key", auto_error=False)

async def get_api_key(
    request: Request,
    api_key_h: Optional[str] = Security(api_key_header),
    api_key_q: Optional[str] = Security(api_key_query),
):
    # Permitir preflight OPTIONS para que CORSMiddleware responda sin validar la API key
    if request.method == "OPTIONS":
        return None

    provided = api_key_h or api_key_q
    if provided == API_KEY:
        return provided
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key")