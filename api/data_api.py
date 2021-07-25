import fastapi
from fastapi import Query
from typing import Optional
from models.data import Data, Time, TimeRequest, FileRequest, File
from services.get_time import get_current_time
from services.get_file import get_named_file

router = fastapi.APIRouter(prefix="/api")

@router.get("/data", response_model=Data) # using the pydantic data model; including the model improves the docs page
def get_std_data(data: Data = fastapi.Depends()): # Depends is required for it to pull data from the query string
    return data

@router.get("/time", response_model=Time)
async def get_time(req: TimeRequest = fastapi.Depends()):
    now = await get_current_time(req)
    current_datetime = now.get("currentDateTime")
    return Time(currentDateTime=current_datetime)

@router.get("/file", response_model=File)
async def get_file(file_req: FileRequest = fastapi.Depends()):
    file = await get_named_file(file_req)
    return File(path=file)

@router.get("/test") # this is a basic test without using the model
def test_data(number: int, index: Optional[int] = None, msg: Optional[str] = Query(None, max_length=15), test: Optional[bool] = True):
    # Query provides validation
    return {
        "number": number,
        "msg": msg,
        "test": test
        }


