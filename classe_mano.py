class Mano:
    def __init__(self):
        self.__carte = []
    
    def aggiungi_carta(self, carta):
        self.__carte.append(carta)

    @property
    def get_carte(self):
        return self.__carte
    
    def svuota(self):
        self.__carte = []

    def __str__(self):
        stringa = ""
        for carta in self.__carte:
            stringa += str(carta) + "\n"
        return stringa