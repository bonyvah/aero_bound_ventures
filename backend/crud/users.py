from sqlmodel import Session, select
from models.users import User


def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()


# def create_user(session: Session, email: str, password: str):

#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user
