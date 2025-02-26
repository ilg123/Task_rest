from sqlalchemy import Column, Integer, String, DateTime, event
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytz

Base = declarative_base()

def set_moscow_time(target):
    moscow_tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(moscow_tz).replace(tzinfo=None)
    if not hasattr(target, 'created_at') or not target.created_at:
        target.created_at = now
    target.updated_at = now

@event.listens_for(Base, 'before_insert', propagate=True)
def before_insert_listener(mapper, connection, target):
    if isinstance(target, Task):
        set_moscow_time(target)

@event.listens_for(Base, 'before_update', propagate=True)
def before_update_listener(mapper, connection, target):
    if isinstance(target, Task):
        set_moscow_time(target)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)