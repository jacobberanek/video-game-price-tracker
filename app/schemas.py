from pydantic import BaseModel

#Pydantic Schemas
class ProductCreate(BaseModel):
    name: str
    category: str
    external_id: str

class ProductResponse(ProductCreate):
    id: int

    class Config: from_attributes = True