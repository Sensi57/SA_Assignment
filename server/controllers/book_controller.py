from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from models.schemas import BookCreate

book_router = APIRouter()

book_svc = None
user_svc = None

@book_router.post("/addBook")
def add_book(request: Request, title: str = Form(...), author: str = Form(...), copies: int = Form(1)):
    email = request.cookies.get("user_email")
    if not email:
        return RedirectResponse(url="/login")
    payload = BookCreate(title=title, author=author, copies=copies)
    book_svc.add_book(payload)
    return RedirectResponse(url="/dashboard", status_code=302)

@book_router.post("/borrowBook")
def borrow_book(user_id: int = Form(...), book_id: int = Form(...)):
    user = user_svc.get_user_by_id(user_id)
    if not user:
        return RedirectResponse(url="/dashboard") 
    success, book = book_svc.borrow_book(user_id, book_id)
    return RedirectResponse(url="/dashboard", status_code=302)