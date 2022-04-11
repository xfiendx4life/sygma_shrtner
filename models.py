from datetime import datetime


class User:
    def __init__(self, id, name, password) -> None:
        self.name = name
        self.password = password
        self.id = id

    def __repr__(self) -> str:
        return str(self.to_dict())

    def to_dict(self):
        d = {}
        d["name"] = self.name
        d["password"] = self.password
        d["id"] = self.id
        return d


class Stats:
    def __init__(self, shortened: str) -> None:
        self.shortened = shortened
        self.redirects = []

    def add_redirect(self):
        self.redirects.append(datetime.now())
