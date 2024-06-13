from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    supercar_id = Column(Integer, ForeignKey('supercars.id'))
    comment_text = Column(String, nullable=False)

    @validates('comment_text')
    def validate_comment_text(self, key, comment_text):
        if not isinstance(comment_text, str):
            raise ValueError("Comment text must be a string")
        if not comment_text:
            raise ValueError("Comment text cannot be empty")
        return comment_text.strip()

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'supercar_id': self.supercar_id,
            'comment_text': self.comment_text
        }