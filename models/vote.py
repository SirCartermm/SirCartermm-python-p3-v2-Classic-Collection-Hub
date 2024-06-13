from sqlalchemy import Column, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from error_handling import errorHandler

Base = declarative_base()

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    supercar_id = Column(Integer, ForeignKey('supercars.id'))
    vote_type = Column(Enum('like', 'dislike'))

    @validates('vote_type')
    def validate_vote_type(self, key, vote_type):
        if vote_type not in ['like', 'dislike']:
            errorHandler.handle_error("Invalid vote type. Must be 'like' or 'dislike'", 400)
        return vote_type

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'supercar_id': self.supercar_id,
            'vote_type': self.vote_type
        }