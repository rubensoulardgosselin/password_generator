import random

class Password:

    def __init__(self, liste, taille, password):
        self.liste_de_caracteres = liste
        self.taille = taille
        self.password = password

    def generation(self):
        for i in range (self.taille) :
            self.password.append(self.liste_de_caracteres[random.randint(0,61)])
        self.password = ''.join(self.password)
        print(self.password)

attributs = Password(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], random.randint(10,15),[])

attributs.generation()


    