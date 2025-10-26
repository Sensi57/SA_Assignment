from copy import deepcopy

class UserRepository:
    def __init__(self):
        self._data = {}
        self._next_id = 1

    def add(self, user):
        user_id = self._next_id
        self._next_id += 1
        stored = {"id": user_id, **deepcopy(user)}
        self._data[user_id] = stored
        return deepcopy(stored)

    def list_all(self):
        return deepcopy(list(self._data.values()))

    def get_by_id(self, user_id):
        return deepcopy(self._data.get(user_id))