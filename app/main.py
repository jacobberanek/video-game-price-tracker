from fastapi import FastAPI, Depends
from app.models import Product
from app.db import engine, Base, SessionLocal, get_db
from .routes import products


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(products.router)
