from copy import deepcopy

class BookRepository:
    def __init__(self):
        self._data = {}
        self._next_id = 1

    def add(self, book):
        book_id = self._next_id
        self._next_id += 1
        stored = {
            "id": book_id,
            "title": book["title"],
            "author": book["author"],
            "copies_total": book.get("copies", 1),
            "copies_available": book.get("copies", 1),
            "borrowed_by": []
        }
        self._data[book_id] = stored
        return deepcopy(stored)

    def list_all(self):
        return deepcopy(list(self._data.values()))

    def get_by_id(self, book_id):
        return deepcopy(self._data.get(book_id))

    def update(self, book_id, updated_book):
        if book_id not in self._data:
            return None
        self._data[book_id] = deepcopy(updated_book)
        return deepcopy(updated_book)