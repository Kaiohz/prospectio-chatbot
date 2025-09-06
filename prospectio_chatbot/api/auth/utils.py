import jwt
import os
from datetime import datetime, timedelta


def create_jwt(identifier: str, metadata: dict) -> str:
    to_encode = {
        "identifier": identifier,
        "metadata": metadata,
        "exp": datetime.now() + timedelta(minutes=60 * 24 * 15),  # 15 days
    }

    encoded_jwt = jwt.encode(
        to_encode, os.getenv("CHAINLIT_AUTH_SECRET"), algorithm="HS256"
    )
    return encoded_jwt