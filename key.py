import random
from password_generator import Password

class key_code:

    def __init__(self, lettre, chiffre, key) -> None:
        self.lettre = lettre
        self.chiffre = chiffre
        self.key = key
  
    def create_key(self):
        lettres = 'abcdefghijklmnopqrstuvwxyz'
        chiffres = '0123456789'
        key = random.choice(lettres) + random.choice(chiffres)
        print("key  ->  ",key)
