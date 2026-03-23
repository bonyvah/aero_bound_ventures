from fastapi import APIRouter, HTTPException, status, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from backend.schemas.users import UserCreate, UserRead
from backend.crud.users import get_user_by_email, create_user
from backend.crud.database import get_session
from backend.utils.email import send_email_async

router = APIRouter(prefix="/api")


@router.post("/register/", response_model=UserRead)
async def register(
    background_tasks: BackgroundTasks,
    user_in: UserCreate,
    session: Session = Depends(get_session),
):
    user = get_user_by_email(session, user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email is already registered",
        )
    user = create_user(session, user_in.email, user_in.password)

    subject = ("Welcome to the Aero Bound Ventures!",)
    recipients = ([user_in.email],)
    body_text = (f"Hello {user_in.email}, \n\nThank you for registering.",)
    background_tasks.add_task(send_email_async, subject, recipients, body_text)

    return user
