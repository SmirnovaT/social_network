from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="api/auth/token")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3Mzk2NzE2MSwiaWF0IjoxNjczOTY3MTYxfQ.cgXhCGZvT99FFVHdHEbDhyvvEwu3Z3uFxYMNgxWkNmU"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
