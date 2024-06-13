from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from error_handling import errorHandler

engine = create_engine('sqlite:///classic_collection_hub.db')
Session = sessionmaker(bind=engine)

def create_db():
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        errorHandler.handle_exception(e)

def get_session():
    try:
        return Session()
    except Exception as e:
        errorHandler.handle_exception(e)
        return None