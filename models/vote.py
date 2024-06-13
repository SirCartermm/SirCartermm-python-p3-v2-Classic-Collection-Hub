from sqlalchemy import Column, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    supercar_id = Column(Integer, ForeignKey('supercars.id'))
    vote_type = Column(Enum('like', 'dislike'))
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'supercar_id': self.supercar_id,
            'vote_type': self.vote_type,
            'created_at': self.created_at
        }