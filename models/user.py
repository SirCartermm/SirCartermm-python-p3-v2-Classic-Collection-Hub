from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    @validates('username')
    def validate_username(self, key, username):
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        if not username:
            raise ValueError("Username cannot be empty")
        return username.strip()

    @validates('email')
    def validate_email(self, key, email):
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if not email:
            raise ValueError("Email cannot be empty")
        if not email.endswith('@example.com'):  # add your own email validation
            raise ValueError("Invalid email address")
        return email.strip()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }