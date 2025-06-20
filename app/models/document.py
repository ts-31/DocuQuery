# models/document.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentMeta(BaseModel):
    filename: str
    filetype: str
    upload_time: datetime
    content: Optional[str]
