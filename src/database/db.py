from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


PG_URL = "postgresql+psycopg2://worker:worker@localhost:5432/FastAPIdb"
engine = create_engine(PG_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()