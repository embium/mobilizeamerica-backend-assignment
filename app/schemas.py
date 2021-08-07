"""FastAPI Pydantic schema
"""
from typing import Optional, Any, Dict
from datetime import datetime
from pydantic import BaseModel, HttpUrl


class Link(BaseModel):
    """Link structure validation
    """
    target: HttpUrl
    created: Optional[datetime] = None
    link: Optional[str] = None
    clicks: Any

    # Required because used with SQLAlchemy
    class Config:
        orm_mode = True


class Click(BaseModel):
    """Click structure validation
    """
    id: int
    created: Optional[datetime] = None

    # Required because used with SQLAlchemy
    class Config:
        orm_mode = True