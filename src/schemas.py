from datetime import date
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    firstname: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    email: str = Field(max_length=50)
    telephone: int 
    birthday: date 

    
class ContactNotes(ContactBase):
    notes: str | None = None


class ContactResponse(ContactBase):
    notes: str | None

    class Config:
        orm_mode = True
