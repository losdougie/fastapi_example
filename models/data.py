from typing import Optional
from pydantic import BaseModel

class Data(BaseModel):
    number: int
    index: Optional[int]
    msg: Optional[str]
    test: Optional[bool] = True

class Time(BaseModel):
    currentDateTime: str

class TimeRequest(BaseModel):
    location: str = "est"

class FileRequest(BaseModel):
    filename: str

class File(BaseModel):
    file: Optional[str]
    filename: Optional[str]
    path: Optional[str]
