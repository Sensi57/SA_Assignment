from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from controllers import book_controller, user_controller
from services.book_service import BookService
from services.user_service import UserService
from models.schemas import UserCreate

app = FastAPI(title="Smart Library System")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

user_svc = UserService()
book_svc = BookService()

book_controller.book_svc = book_svc
book_controller.user_svc = user_svc
user_controller.user_svc = user_svc

app.include_router(user_controller.user_router, prefix="/api")
app.include_router(book_controller.book_router, prefix="/api")

# --- Страницы ---
@app.get("/", response_class=HTMLResponse)
def redirect_to_login():
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, email: str = Form(...)):
    user = next((u for u in user_svc.list_users() if u["email"] == email), None)
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "User not found. Please register."},
        )
    response = RedirectResponse(url="/dashboard", status_code=302)
    response.set_cookie("user_email", email)
    return response

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
def register_user(request: Request, name: str = Form(...), email: str = Form(...)):
    user_data = UserCreate(name=name, email=email)
    user_svc.register_user(user_data)
    return RedirectResponse(url="/login", status_code=302)

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    email = request.cookies.get("user_email")
    if not email:
        return RedirectResponse(url="/login")

    user = next((u for u in user_svc.list_users() if u["email"] == email), None)
    if not user:
        return RedirectResponse(url="/login")

    books = book_svc.list_books()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "user": user, "books": books},
    )