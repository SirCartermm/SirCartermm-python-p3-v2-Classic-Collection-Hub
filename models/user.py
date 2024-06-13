from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from error_handling import errorHandler

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            errorHandler.handle_error("Username cannot be empty", 400)
        return username

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            errorHandler.handle_error("Email cannot be empty", 400)
        return email

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }