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
        print("code -> ",self.password)

    def get_password(self):
        return Password




    