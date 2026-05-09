from sqlalchemy.orm import Session
from models.your_model import Item

def get_all(db: Session):
    return db.query(Item).all()

def get_by_id(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()

def create_item(db: Session, item):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item