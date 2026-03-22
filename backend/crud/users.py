from sqlmodel import Session, select
from models.users import User
from utils.security import hash_password


def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()


def create_user(session: Session, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
