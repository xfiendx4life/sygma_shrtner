import json
import os

storage = {}
users_storage = {}

def store_users():
    '''Stores users data to json file'''
    with open('./users_storage.json', 'w') as f:
        json.dump(users_storage, f)


def store_data():
    '''Stores data to json file'''
    with open('./storage.json', 'w') as f:
        json.dump(storage, f)


def get_data_from_storage():
    '''Loads data from json file to storage dictionary'''
    if not os.path.exists('./storage.json'):
        return 
    with open('./storage.json') as f:
        u = json.load(f)
    for k, v in u.items():
        storage[k] = v

def get_users_from_storage():
    '''Loads users data from json file to storage dictionary'''
    if not os.path.exists('./users_storage.json'):
        return 
    with open('./users_storage.json') as f:
        u = json.load(f)
    for k, v in u.items():
        users_storage[k] = v