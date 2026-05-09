from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories import your_repo

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return your_repo.get_all(db)

@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    return your_repo.get_by_id(db, id)