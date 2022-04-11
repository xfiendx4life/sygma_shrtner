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