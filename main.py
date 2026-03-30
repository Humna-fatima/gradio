from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello World"} 

from fastapi import FastAPI
from routers import your_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(your_router.router)