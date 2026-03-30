from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    value: float
    category: str

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int
    class Config:
        from_attributes = True