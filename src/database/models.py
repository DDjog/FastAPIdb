from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from src.database.db import engine

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    telephone = Column(Integer)
    birthday = Column(Date)
    notes = Column(Text, nullable=True)


Base.metadata.create_all(bind=engine)