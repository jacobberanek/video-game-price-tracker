from fastapi import FastAPI, Depends
from app.models import Product
from app.db import engine, Base, SessionLocal, get_db
from .routes import products
from .services.steam_fetcher import SteamPriceFetcher
import logging


logging.basicConfig(
    level=logging.INFO, #CHANGE LOGGING LEVEL AT END OF DEVELOPMENT
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(products.router)

fetcher = SteamPriceFetcher()
price = fetcher.price_fetch("1145360")
print(f"{fetcher.get_vendor_name()}: ${price}")


