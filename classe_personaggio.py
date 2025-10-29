from classe_arma import Arma

class Personaggio:
    def __init__(self, nome: str, vita_massima: int, forza: int, destrezza: int):
        self.__nome = nome
        self.__vita_massima = vita_massima
        self.__vita = self.__vita_massima
        self.__forza = forza 
        self.__destrezza = destrezza
        self.__arma = None

    #Funzione che assegna un'arma al personaggio
    def equipaggia(self, arma: Arma):
        self.__arma = arma

    #Funzione che calcola il modificatore 
    def modificatore(self, valore: int):
        return ((valore - 10) // 2)
    
    #Funzione che controlla se il personaggio è ancora vivo
    def e_vivo(self) -> bool:
        return self.__vita > 0
        
    #Funzione che riduce la vita del personaggio
    def subisci(self, danno: int) -> int:
        danno_effettivo = max(0, danno)
        self.__vita = max(0, self.__vita - danno_effettivo)
        return danno_effettivo
    
    #Funzione che gestisce l'attacco di un personaggio verso un altro
    def attacca(self, nemico: "Personaggio") -> int:
        #Se non ha un’arma equipaggiata, danno base = 1
        if not self.__arma:
            danno = 1
        else:
            #Danno casuale dell’arma
            danno = self.__arma.get_danno()
            #Aggiunge modificatore di forza o destrezza in base al tipo
            if self.__arma.tipo == "mischia":
                danno += self.modificatore(self.__forza)
            else: 
                danno += self.modificatore(self.__destrezza)
        danno = max(0, danno)
        return nemico.subisci(danno)

    #Imposto le "property" (getter e setter) per il nome 
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    #Imposto le "property" (getter e setter) per la vita
    @property
    def vita(self):
        return self.__vita

    @vita.setter
    def vita(self, vita: int):
        self.__vita = max(0, min(vita, self.__vita_massima))

    #Imposto le "property" (getter e setter) per la vita_massima 
    @property
    def vita_massima(self):
        return self.__vita_massima

    @vita_massima.setter
    def vita_massima(self, vita_massima: int):
        if vita_massima > 0:
            self.__vita_massima = vita_massima
            if self.__vita > vita_massima:
                self.__vita = vita_massima

    #Imposto le "property" (getter e setter) per la forza 
    @property
    def forza(self):
        return self.__forza

    @forza.setter
    def forza(self, forza: int):
        self.__forza = forza

    #Imposto le "property" (getter e setter) per la destrezza 
    @property
    def destrezza(self):
        return self.__destrezza

    @destrezza.setter
    def destrezza(self, destrezza: int):
        self.__destrezza = destrezza

    #Imposto le "property" (getter e setter) per l'arma
    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, arma: Arma):
        self.__arma = arma

    def __str__(self):
        return f"{self.__nome}: {self.__vita}/{self.__vita_massima} HP"