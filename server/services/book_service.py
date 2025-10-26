from repositories.book_repository import BookRepository
from models.schemas import BookCreate

class BookService:
    def __init__(self):
        self.repo = BookRepository()

    def add_book(self, payload: BookCreate):
        book = {
            "title": payload.title,
            "author": payload.author,
            "copies": payload.copies or 1
        }
        return self.repo.add(book)

    def list_books(self):
        return self.repo.list_all()

    def borrow_book(self, user_id: int, book_id: int):
        book = self.repo.get_by_id(book_id)
        if not book:
            return False, "Book not found"
        if book["copies_available"] <= 0:
            return False, "No copies available"

        book["copies_available"] -= 1
        book["borrowed_by"].append(user_id)
        self.repo.update(book_id, book)
        return True, book