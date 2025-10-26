from fastapi import APIRouter
from models.schemas import UserCreate
from services.user_service import UserService

user_router = APIRouter()
user_svc = UserService()

@user_router.post("/registerUser")
def register_user(payload: UserCreate):
    return {"status": "ok", "user": user_svc.register_user(payload)}

@user_router.get("/listUsers")
def list_users():
    return {"users": user_svc.list_users()}