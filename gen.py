import random
from string import ascii_letters

SYMBOLS = '-._~'

def generate(raw: str) -> str:
    l_raw = list(raw)
    random.shuffle(l_raw)
    l_raw = list(filter(lambda x: x in ascii_letters or x in SYMBOLS, l_raw))
    return ''.join(l_raw[:20])
