import json

storage = {}
users_storage = {}

def store_users():
    with open('./users_storage.json', 'w') as f:
        json.dump(users_storage, f)

# TODO: Написать функцию для хранения данных из словаря storage
# * Там хранятся ссылки на сайты и сокращенные ссылки
def store_data():
    pass

# TODO: написать функцию для получения данных из файла и записи в словарь
def get_data_from_storage():
    pass

def get_users_from_storage():
    with open('./users_storage.json') as f:
        u = json.load(f)
    for k, v in u.items():
        users_storage[k] = v