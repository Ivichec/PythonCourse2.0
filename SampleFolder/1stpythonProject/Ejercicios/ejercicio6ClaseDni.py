class Dni:
    def __init__(self, numero=0):
        self.numero = numero
        self.letra = ""
    def letraDni(self):
        chars = ["t", "r", "w", "a", "g", "m", "t", "y", "f", "p", "d", "x", "b", "n", "j", "z", "s", "q", "v", "h",
                 "l", "c", "k", "e"]
        self.letra = chars[(self.numero % 23)+1].upper()
        return self.letra
