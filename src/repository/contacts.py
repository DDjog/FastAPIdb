from datetime import timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func, and_, Interval
from typing import List
from src.database.models import Contact
from src.schemas import ContactBase, ContactResponse


def age_in_years_for_days_ahead(birthday, next_days: int = 0):
    stmt = func.age(
        (birthday - func.cast(timedelta(next_days), Interval)) if next_days != 0 else birthday
    )
    stmt = func.date_part("year", stmt)

    return stmt


def has_birthday_next_days(birthday, next_days: int = 0):
    return age_in_years_for_days_ahead(birthday, next_days) > age_in_years_for_days_ahead(birthday)


async def get_contacts_birthday_ahead(days: int, db: Session) -> List[Contact]:

    contacts = db.query(Contact).filter(has_birthday_next_days(Contact.birthday, days)).all()

    if contacts is None:
        return None

    return contacts


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def get_contact_notes(contact_id: int, db: Session) -> ContactResponse:
    contact=db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact is None:
        return None
    
    return contact


async def get_contacts_by_email(contact_email: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.email.ilike(f'%{contact_email}%')).all()


async def get_contacts_by_firstname(firstname: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.firstname.ilike(f'%{firstname}%')).all()


async def get_contacts_by_secondname(secondname: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.secondname.ilike(f'%{secondname}%')).all()


async def get_contacts_by_first_and_second_name(firstname: str, secondname: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter( and_(Contact.firstname.ilike(f'%{firstname}%'), Contact.secondname.ilike(f'%{secondname}%')) ).all()


async def create_contact(body: ContactBase, db: Session) -> Contact:
    contact = Contact( firstname=body.firstname, 
                       lastname = body.lastname,
                       email = body.email,
                       telephone = body.telephone,
                       birthday = body.birthday )
    db.add( contact )
    db.commit()
    db.refresh( contact )
    
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact:
        db.delete(contact)
        db.commit()
        
    return contact


async def update_contact(contact_id: int, body: ContactBase, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact:
        
        contact.firstname = body.firstname
        contact.lastname = body.lastname
        contact.email = body.email
        contact.telephone = body.telephone
        contact.birthday = body.birthday
        
        db.commit()
        
    return contact


async def update_contact_notes(contact_id: int, notes: str, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact:
        
        contact.notes = notes
        
        db.commit()
        
    return contact

