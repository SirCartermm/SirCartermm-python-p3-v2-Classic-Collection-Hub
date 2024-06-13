from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///classic_collection_hub.db')
Session = sessionmaker(bind=engine)

def create_db():
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Error creating database: {e}")

def get_session():
    try:
        return Session()
    except Exception as e:
        print(f"Error creating session: {e}")
        return None
