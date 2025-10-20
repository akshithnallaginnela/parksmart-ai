from app.models.user import User
from passlib.context import CryptContext
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain, hashed):
    return pwd.verify(plain, hashed)

def get_password_hash(password):
    return pwd.hash(password)
