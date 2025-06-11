from sqlalchemy import Column, Integer, String, Boolean
from config import Base
from werkzeug.security import check_password_hash, generate_password_hash

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def verify_password(self, password: str) -> bool:
        """Verify the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)
    
    def set_password(self, password: str) -> None:
        """Set the password hash for the user."""
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active}, is_superuser={self.is_superuser})>"