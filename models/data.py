from typing import Optional
from pydantic import BaseModel

class Data(BaseModel):
    number: int
    index: Optional[int]
    msg: Optional[str]
    test: Optional[bool] = True
