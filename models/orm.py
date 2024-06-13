from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///classic_collection_hub.db')
Session = sessionmaker(bind=engine)

def create_db():
    Base.metadata.create_all(engine)

def get_session():
    return Session()