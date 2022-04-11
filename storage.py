import json
import os

storage = {}
users_storage = {}
stats_storage ={}

def store_data(storage_path:str, storage:dict):
    """Stores data to json file"""
    with open(storage_path, "w") as f:
        json.dump(storage, f)


def get_data_from_storage(storage_path:str, storage:dict):
    """Loads data from json file to storage dictionary"""
    if not os.path.exists(storage_path):
        return
    with open(storage_path) as f:
        u = json.load(f)
    for k, v in u.items():
        storage[k] = v

