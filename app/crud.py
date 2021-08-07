"""FastAPI CRUD file
"""
from typing import Optional
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from random import sample
from string import ascii_letters, digits


def get_link(db: Session, link: str, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """Retrieve link information by link ID
    """
    link = db.query(models.Link).filter(models.Link.link == link).first()
    if link:
        if start_date and end_date:
            try:
                start_date = datetime.fromisoformat(start_date).date()
                end_date = datetime.fromisoformat(end_date).date()
            except ValueError:
                return link
            clicks = []
            for click in link.clicks:
                    if start_date <= click.created.date() <= end_date:
                        clicks.append(click)
            link.clicks.clear()
            link.clicks = clicks
        return link


def create_link(db: Session, link: schemas.Link):
    """Create the link
    """
    # Generates random string of 7 chars with letters and digits
    if not link.link:
        chars = ascii_letters + digits
        link.link = ''.join(sample(chars, 7))
    
    db_link = models.Link(
        link=link.link,
        target=link.target
    )
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def count_clicks(db: Session, link: schemas.Link):
    """Count clicks of the link"""
    click = models.Click(link_id=link.id)
    link.amount = len(link.clicks) + 1
    db.add(click)
    db.commit()

def delete_link(db: Session, link: str):
    """Delete the link
    """
    # SQLAlchemy magic :)
    db_link = db.query(models.Link).filter(models.Link.link == link).first()
    db.delete(db_link)
    db.commit()
    return {}
