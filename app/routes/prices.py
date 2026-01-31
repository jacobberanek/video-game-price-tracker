from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db, SessionLocal, engine, Base
from .. import schemas, models
from ..services.steam_fetcher import SteamPriceFetcher

router = APIRouter(prefix="/prices", tags=["prices"])

@router.post("/update/{product_id}", response_model = schemas.PriceHistoryResponse)
def update_product_price(product_id: int, db: Session = Depends(get_db)):
    """Fetch and store current price for a product."""
    #Grabs row for product to update
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail = "Product not found")
    
    #Grabs external_id (steam id for now) from product row
    external_id = product.external_id

    vendor_name = "Steam"

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
        product_id = product.id,
        vendor_id = vendor.id,
        price = current_price
    )
    db.add(price_record)
    db.commit()
    db.refresh(price_record)


    return {
        "product_id": product.id,
        "product_name": product.name,
        "vendor": vendor.name,
        "price": current_price,
        "success": True
    }
