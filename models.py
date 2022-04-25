from datetime import datetime

from flask import redirect


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
    # TODO: Добавить инициализацию объекта из словаря
    def __init__(self, shortened: str = "", d: dict = {}) -> None:
        self.shortened = shortened
        if d == {}:
            self.redirects = 0
        else:
            self.redirects = d["redirects"]
            self.last_rdr = datetime.strptime(d["last_redirect"], "%d.%m.%y")

    def add_redirect(self):
        self.redirects += 1

    def last_redirect(self):
        self.last_rdr = datetime.now()

    def to_dict(self):
        return {
            "last_redirect": datetime.strftime(self.last_rdr, "%d.%m.%y"),
            "redirects": self.redirects,
        }
