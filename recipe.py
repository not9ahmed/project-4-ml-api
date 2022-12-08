from pydantic import BaseModel
from typing import Optional

class Recipe(BaseModel):
    name_en: str
    image: Optional[str] = None