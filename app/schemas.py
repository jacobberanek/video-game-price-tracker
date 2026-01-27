from pydantic import BaseModel
from datetime import datetime

#Pydantic Schemas
class ProductCreate(BaseModel):
    name: str
    category: str
    external_id: str

class ProductResponse(ProductCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config: from_attributes = True



class VendorCreate(BaseModel):
    name: str
    api_endpoint: str

class VendorResponse(VendorCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config: from_attributes = True



class PriceHistoryCreate(BaseModel):
    price: float
    product_id: int
    vendor_id: int


class PriceHistoryResponse(PriceHistoryCreate):
    id: int
    created_at: datetime

    class Config: from_attributes = True