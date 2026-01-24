from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db, SessionLocal, engine, Base
from .. import schemas, models

router = APIRouter()

@router.post('/products', response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.delete("/products/{product_id}")
def delete_product(product_id : int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail = "Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product Deleted"}