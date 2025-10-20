from classe_arma import Arma

class Personaggio:
    def __init__(self, nome:str, vita_massima:int, forza:int, destrezza:int):
        self.__nome = nome
        self.__vita_massima = vita_massima
        self.__vita = self.__vita_massima
        self.__forza = forza 
        self.__destrezza = destrezza
        self.__arma = None

    #Funzione che assegna un'arma al personaggio
    def equipaggia(self, arma: Arma):
        self.__arma = arma

    #Funzione che calcola il modifcatore 
    def modificatore(self, valore: int):
        return ((valore - 10) // 2)
    
    #Funzione che controlla se il personaggio è ancora vivo
    def e_vivo(self) -> bool:
        if self.__vita > 0:
            return True
        else:
            return False
        
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
            if self.__arma.get_tipo() == "mischia":
                danno += self.modificatore(self.__forza)
            else: 
                danno += self.modificatore(self.__destrezza)
        danno = max(0, danno)
        
        #Applica il danno al nemico
        return nemico.subisci(danno)

    #GETTER (è un metodo che serve per leggere un attributo privato (cioè nascosto))
    def get_nome(self):
        return self.__nome

    def get_vita(self):
        return self.__vita

    def get_vita_massima(self):
        return self.__vita_massima

    def get_forza(self):
        return self.__forza

    def get_destrezza(self):
        return self.__destrezza

    def get_arma(self):
        return self.__arma

    #SETTER (è un metodo che serve per modificare (cioè impostare) un attributo privato)
    def set_nome(self, nome):
        self.__nome = nome

    def set_vita(self, vita):
        self.__vita = max(0, min(vita, self.__vita_massima))

    def set_vita_massima(self, vita_massima):
        if vita_massima > 0:
            self.__vita_massima = vita_massima
            if self.__vita > vita_massima:
                self.__vita = vita_massima

    def set_forza(self, forza):
        self.__forza = forza

    def set_destrezza(self, destrezza):
        self.__destrezza = destrezza

    def set_arma(self, arma: Arma):
        self.__arma = arma

    def __str__(self):
        return f"{self.__nome}: {self.__vita}/{self.__vita_massima} HP"