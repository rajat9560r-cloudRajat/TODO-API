import jwt
from jwt import InvalidTokenError
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
load_dotenv()

ALGORITHM = os.getenv("ALGO")
SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRATION_TIME  = 30









def create_access_token(data : dict):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = EXPIRATION_TIME)
    payload["exp"] = expire
    access_token = jwt.encode(payload, SECRET_KEY, algorithm = ALGORITHM)
    print(payload)
    return access_token

