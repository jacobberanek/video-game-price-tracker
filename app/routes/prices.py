from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..db import get_db, SessionLocal, engine, Base
from .. import schemas, models
from ..services.steam_fetcher import SteamPriceFetcher
from typing import Optional
from datetime import date

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

@router.post("/update-all")
def update_all_prices(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()

    results = []
    success = 0
    fail = 0
    steam_fetcher = SteamPriceFetcher()
    for product in products:
        price = steam_fetcher.price_fetch(product.external_id)

        if price is None:
            fail += 1
            results.append({"product_id": product.id, "success": False, "error": "Price not found"})
        else:
            success += 1
            results.append({"product_id": product.id, "success": True, "price": price})
    return {
        "total": len(products),
        "succeeded": success,
        "failed": fail,
        "results": results
    }



@router.get("/{product_id}", response_model = list[schemas.PriceHistoryResponse])
def get_prices(
    product_id: int,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    
    query = db.query(models.Price_History).filter(models.Price_History.product_id == product_id)
    
    if start_date:
        query = query.filter(models.Price_History.created_at >= start_date)
    if end_date:
        query = query.filter(models.Price_History.created_at <= end_date)

    return query.all()