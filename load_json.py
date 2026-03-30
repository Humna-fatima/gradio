import json
from database import SessionLocal, engine, Base
from models.your_model import Item

Base.metadata.create_all(bind=engine)

with open("data/your_data.json") as f:
    data = json.load(f)

db = SessionLocal()
for row in data:
    item = Item(
        name=row["name"],       # ← change keys
        value=row["value"],
        category=row["category"]
    )
    db.add(item)
db.commit()
db.close()
print("Done!")


#Run once: python load_json.py — then never again unless data changes