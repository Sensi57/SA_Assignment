from repositories.user_repository import UserRepository
from models.schemas import UserCreate

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def register_user(self, payload: UserCreate):
        user = {"name": payload.name, "email": payload.email}
        return self.repo.add(user)

    def list_users(self):
        return self.repo.list_all()

    def get_user_by_id(self, user_id: int):
        return self.repo.get_by_id(user_id)