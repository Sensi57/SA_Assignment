from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class BookCreate(BaseModel):
    title: str
    author: str
    copies: Optional[int] = 1

class BorrowRequest(BaseModel):
    user_id: int
    book_id: int