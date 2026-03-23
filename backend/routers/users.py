from fastapi import APIRouter, HTTPException, status
from backend.schemas.users import UserCreate, UserRead
from backend.crud.users import get_user_by_email, create_user
from backend.utils.email import send_email_async

router = APIRouter(prefix="/api")


@router.post("/register/", response_model=UserRead)
async def register(user_in: UserCreate):
    user = get_user_by_email(user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email is already registered",
        )
    user = create_user(email=user_in.email, password=user_in.password)

    await send_email_async(
        subject="Welcome to the Aero Bound Ventures!",
        recipient=user_in.email,
        body=f"Hello {user_in.email}, \n\nThank you for registering.",
    )

    return user
