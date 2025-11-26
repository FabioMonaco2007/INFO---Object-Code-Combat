import random

class Mazzo:
    def __init__(self, lista_carte):
        self.__carte = lista_carte

    @property
    def carte(self):
        return self.__carte

    def mescola(self):
        random.shuffle(self.__carte)

    def pesca(self):
        carta_rimossa = self.__carte.pop()
        return carta_rimossa