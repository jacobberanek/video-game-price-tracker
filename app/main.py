from fastapi import FastAPI
from app.models import Product
from app.db import engine, Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
