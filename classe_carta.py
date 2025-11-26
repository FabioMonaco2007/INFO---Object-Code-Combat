class Carta:
    def __init__(self, seme: str, rango: str):
        self.__seme = seme
        self.__rango = rango

    @property
    def seme(self):
        return self.__seme

    @property
    def rango(self):
        return self.__rango

    @property
    def valore(self) -> int:
        if self.__rango in ["J", "Q", "K"]:
            return 10
        elif self.__rango == "A":
            return 11 
        else:
            return int(self.__rango)
        
    def __str__(self):
        return f"Seme: {self.__seme}, Valore: {self.__rango}"