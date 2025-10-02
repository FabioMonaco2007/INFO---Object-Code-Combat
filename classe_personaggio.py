from classe_arma import Arma

class Personaggio:
    def __init__(self, nome:str, vita_massima:int, forza:int, destrezza:int):
        self.nome = nome
        self.vita_massima = vita_massima
        self.vita = self.vita_massima
        self.forza = forza 
        self.destrezza = destrezza
        self.arma = None

    def equipaggia(self, arma: Arma):
        self.arma = arma

    def modificatore(self, valore: int):
        return ((valore - 10) // 2)
    
    def e_vivo(self) -> bool:
        if self.vita > 0:
            return True
        else:
            return False