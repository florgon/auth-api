"""
    User agent CRUD utils for the database.
"""

# Libraries.
from sqlalchemy.orm import Session

# Models.
from app.database.models.user_agent import UserAgent


def get_or_create_by_string(db: Session, user_agent_string: str) -> UserAgent:
    """ Returns user agent by it`s string. """
    user_agent = db.query(UserAgent).filter(UserAgent.user_agent == user_agent_string).first()
    if user_agent is None:
        user_agent = UserAgent(user_agent=user_agent_string)
        db.add(user_agent)
        db.commit()
        db.refresh(user_agent)
    return user_agent