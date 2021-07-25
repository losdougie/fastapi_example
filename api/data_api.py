import fastapi
from fastapi import Query
from typing import Optional
from models.data import Data

router = fastapi.APIRouter()

@router.get("/api/data", response_model=Data) # using the pydantic data model; including the model improves the docs page
def get_std_data(data: Data = fastapi.Depends()): # Depends is required for it to pull data from the query string
    return data

@router.get("/api/test") # this is a basic test without using the model
def test_data(number: int, index: Optional[int] = None, msg: Optional[str] = Query(None, max_length=15), test: Optional[bool] = True):
    # Query provides validation
    return {
        "number": number,
        "msg": msg,
        "test": test
        }


