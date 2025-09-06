import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from api.auth.utils import create_jwt
import uuid

auth_router = APIRouter()
logger = logging.getLogger(__name__)

@auth_router.get("/token")
async def get_token():
    """
    Generate a unique session ID and create a JWT token.

    Returns:
        JSONResponse: A JSON response containing the JWT token and session ID.
            - token (str): JWT token for authentication
            - session_id (str): Unique session identifier (UUID)

    Raises:
        HTTPException: If token generation fails, returns a 500 error with details.
    """
    try:
        session_uuid = str(uuid.uuid4())
        token = create_jwt(session_uuid, {"name": f"Copilot Front {session_uuid}"})
        return JSONResponse(
            content={"token": token, "session_id": session_uuid}, status_code=200
        )
    except Exception as e:
        logger.exception("Error occurred while generating token")
        raise HTTPException(status_code=500, detail=f"Error occurred while generating token: {str(e)}")