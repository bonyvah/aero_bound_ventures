from fastapi import APIRouter, HTTPException
from schemas.users import UserCreate, UserRead
from crud.users import get_user_by_email, create_user

router = APIRouter(prefix="/api")


@router.post("/register/", response_model=UserRead)
def register(user_in: UserCreate):
    user = get_user_by_email(user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="email is already registered")
    user = create_user(email=user_in.email, password=user_in.password)

    return user
