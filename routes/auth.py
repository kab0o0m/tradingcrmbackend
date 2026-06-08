from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.user import UserCreate
from schemas.user import UserLogin
from utils.auth import (
    verify_password,
    create_access_token
)
from models.user import User

from utils.auth import hash_password
from utils.auth import get_current_user

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )

    if existing_user:
        return {
            "message": "Email already exists"
        }

    new_user = User(
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "email": new_user.email
    }

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:
        return {
            "message": "Invalid credentials"
        }

    if not verify_password(
        user.password,
        db_user.password_hash
    ):
        return {
            "message": "Invalid credentials"
        }

    token = create_access_token(
        db_user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
def me(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }