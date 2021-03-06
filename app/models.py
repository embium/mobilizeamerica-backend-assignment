"""SQLAlchemy models
"""
from sqlalchemy import Column, String, Text, Integer, JSON, DateTime,\
    ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Link(Base):
    """SQLAlchemy definition for links table
    """
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    link = Column(String(20), unique=True, index=True, nullable=False)
    target = Column(Text, index=True, nullable=False)
    created = Column(DateTime, default=datetime.now)
    amount = Column(Integer, default=0)
    clicks = relationship('Click')


class Click(Base):
    __tablename__ = "clicks"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    created = Column(DateTime, default=datetime.now)
    ip_address = Column(String(39), index=True, nullable=False)
    link_id = Column(Integer, ForeignKey('links.id'))