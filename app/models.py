from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db import Base

#Database Tables
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    category = Column(String, nullable=False)
    external_id = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    prices = relationship("Price_History", back_populates="product")


class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    api_endpoint = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    prices = relationship("Price_History", back_populates="vendor")


class Price_History(Base):
    __tablename__ = "price_history"
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="RESTRICT"))
    vendor_id = Column(Integer, ForeignKey("vendors.id", ondelete="RESTRICT"))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    vendor = relationship("Vendor", back_populates="prices")
    product = relationship("Product", back_populates="prices")



