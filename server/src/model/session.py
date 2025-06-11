from sqlalchemy import Column, Integer, String, Boolean
from config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)
    session_id = Column(String(50), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="sessions")

    def __repr__(self):
        return f"<Session(id={self.id}, session_id={self.session_id}, user_id={self.user_id}, is_active={self.is_active})>"