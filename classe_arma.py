import random

class Arma:
    def __init__(self, nome:int, danno_minimo:int, danno_massimo:int, tipo:str):
        self.__nome = nome
        #Controllo dei limiti del danno (minimo e massimo)
        if danno_minimo >= 1:
            self.__danno_minimo = danno_minimo
        else:
            print("Attenzione!! Il danno minimo non è maggiore/uguale ad 1.")
            self.__danno_minimo = 1
        
        if danno_massimo >= danno_minimo:
            self.__danno_massimo = danno_massimo
        else:
            print("Attenzione!! Il danno massimo è più piccolo della condizione.")
            self.__danno_massimo = self.__danno_minimo + 1

        #Controllo di che tipo di arma si tratta
        if tipo == "mischia" or tipo == "distanza":
            self.__tipo = tipo
        else:
            print("ERRORE! Il tipo dev'essere mischia o distanza")
            self.__tipo = "mischia" #Arma che viene inserita di default

    #GETTER (è un metodo che serve per leggere un attributo privato (cioè nascosto))
    def get_nome(self):
        return self.__nome
    
    def get_danno_minimo(self):
        return self.__danno_minimo
    
    def get_danno_massimo(self):
        return self.__danno_massimo
    
    def get_tipo(self):
        return self.__tipo

    #SETTER (è un metodo che serve per modificare (cioè impostare) un attributo privato)
    def set_nome(self, nome):
        self.__nome = nome

    def set_danno_minimo(self, danno_minimo):
        if danno_minimo >= 1:
            self.__danno_minimo = danno_minimo
        else:
            print("Attenzione!! Il danno minimo non è maggiore/uguale ad 1.")
            self.__danno_minimo = 1

    def set_danno_massimo(self, danno_massimo):
        if danno_massimo >= self.__danno_minimo:
            self.__danno_massimo = danno_massimo
        else:
            print("Attenzione!! Il danno massimo è più piccolo della condizione.")
            self.__danno_massimo = self.__danno_minimo + 1

    def set_tipo(self, tipo):
        if tipo == "mischia" or tipo == "distanza":
            self.__tipo = tipo
        else:
            print("ERRORE! Il tipo dev'essere mischia o distanza")
            self.__tipo = "mischia"

    def get_danno(self) -> int:
        numero_casuale = random.randint(self.__danno_minimo, self.__danno_massimo)
        return numero_casuale
    
    def __str__(self):
        return f"Nome: {self.__nome}, ({self.__danno_minimo}, {self.__danno_massimo}), Tipo: {self.__tipo}"
