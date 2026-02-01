from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db, SessionLocal, engine, Base
from .. import schemas, models
from ..services.steam_fetcher import SteamPriceFetcher

router = APIRouter(prefix="/prices", tags=["prices"])

@router.post("/update/{product_id}", response_model = schemas.PriceHistoryResponse)
def update_product_price(product_id: int, vendor_name: str="Steam", db: Session = Depends(get_db)):
    """Fetch and store current price for a product."""
    #Grabs row for product to update
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail = "Product not found")
    
    #Grabs external_id (steam id for now) from product row
    external_id = product.external_id

    steam_fetcher = SteamPriceFetcher()
    current_price = steam_fetcher.price_fetch(external_id)

    if current_price is None:
        raise HTTPException(status_code=500, detail = "Internal server error")

    #Query for steam vendor (HARDCODED FOR NOW) ********************Change later**************************
    #Future: Add steam vendor creation if not found
    vendor = db.query(models.Vendor).filter(models.Vendor.name == vendor_name).first()
    if not vendor:
        raise HTTPException(status_code=404, detail = "Vendor not found")

    price_record = models.Price_History(
        price = current_price,
        product_id = product.id,
        vendor_id = vendor.id,
    )
    db.add(price_record)
    db.commit()
    db.refresh(price_record)


    return price_record

@router.get("/{product_id}", response_model = list[schemas.PriceHistoryResponse])
def get_prices(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.Price_History).filter(models.Price_History.product_id).all()
