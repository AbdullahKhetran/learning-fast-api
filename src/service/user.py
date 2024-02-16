from datetime import timedelta, datetime
import os
from jose import jwt
from model.user import User

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data

# Auth stuff

from passlib.context import CryptContext

# TODO: change key to production key
SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    """Hash <plain> and compare with <hash> from database"""
    return pwd_context.verify(plain, hash)


def get_hash(plain: str) -> str:
    """Return the hash of a <plain> string"""
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    """Return username from JWT access <token>"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except jwt.JWTERROR:
        return None
    return username


def lookup_user(username: str) -> User | None:
    """Return a matching User from the database for <name>"""
    if (user := data.get(username)):
        return User
    return None


def get_current_user(token: str) -> User | None:
    """Decode an 0Auth access <token> and return User"""
    if not (username := get_jwt_username(token)):
        return None
    if (user := lookup_user(username)):
        return user
    return None


def auth_user(name: str, plain: str) -> User | None:
    """Authenticate user <name> and <plain> password"""
    if not (user := lookup_user(name)):
        return None
    if not verify_password(plain, user.hash):
        return None
    return user


def create_access_token(data: dict,
                        expires: timedelta | None = None
                        ):
    """Return a JWT access token"""
    src = data.copy()
    now = datetime.utcnow()
    if not expires:
        expires = timedelta(minutes=15)
    src.update({"exp": now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# CURD passthrough stuff

def get_all() -> list[User]:
    return data.get_all()


def get_one(name) -> User:
    return data.get_one(name)


def create(user: User) -> User:
    return data.create(user)


def modify(name: str, user: User) -> User:
    return data.modify(name, user)


def delete(name: str) -> None:
    return data.delete(name)
