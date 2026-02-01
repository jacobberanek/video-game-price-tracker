from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db, SessionLocal, engine, Base
from .. import schemas, models

router = APIRouter(prefix="/vendors", tags=["vendors"])

@router.post("/", response_model=schemas.VendorResponse)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):

    existing_vendor = db.query(models.Vendor).filter_by(name=vendor.name).first()
    if existing_vendor:
        raise HTTPException(status_code=400, detail="Vendor Already Exists")
    else:
        db_vendor = models.Vendor(**vendor.dict())
        db.add(db_vendor)
        db.commit()
        db.refresh(db_vendor)
        return db_vendor

@router.get("/", response_model=list[schemas.VendorResponse])
def get_vendors(db: Session = Depends(get_db)):
    return db.query(models.Vendor).all()

@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=400, detail = "Vendor not found")
    
    db.delete(vendor)
    db.commit()
    return {"message": "Vendor Deleted"}
