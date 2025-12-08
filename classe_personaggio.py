import random
from classe_arma import Arma

class Personaggio:
    def __init__(self, nome: str, vita_massima: int, forza: int, destrezza: int):
        #Validazione dei parametri numerici:
        #1)Solleva ValueError se vita_massima, forza o destrezza sono <= 0
        if vita_massima <= 0:
            raise ValueError("vita_massima deve essere > 0.")
        if forza <= 0:
            raise ValueError("forza deve essere > 0.")
        if destrezza <= 0:
            raise ValueError("destrezza deve essere > 0.")

        self.__nome = nome
        self.__vita_massima = vita_massima
        self.__vita = self.__vita_massima
        self.__forza = forza 
        self.__destrezza = destrezza
        self.__arma = None
        self.__pozioni = []

    #Funzione che assegna un'arma al personaggio
    def equipaggia(self, arma: Arma):
        #Controllo duck-typing sull'oggetto arma:
        #1)Solleva TypeError se l'oggetto non ha i metodi/attributi attesi
        if not (hasattr(arma, "get_danno") and (hasattr(arma, "tipo") or hasattr(arma, "get_type"))):
            raise TypeError("Oggetto non equipaggiabile, non è un’arma valida.")
        self.__arma = arma

    #Funzione che calcola il modificatore 
    def modificatore(self, valore: int):
        return ((valore - 10) // 2)
    
    #Funzione che controlla se il personaggio è ancora vivo
    def e_vivo(self) -> bool:
        return self.__vita > 0
        
    #Funzione che riduce la vita del personaggio
    def subisci(self, danno: int) -> int:
        #Validazioni:
        #1)Solleva TypeError se danno non è intero
        #2)Solleva ValueError se danno è negativo
        if not isinstance(danno, int):
            raise TypeError("danno deve essere un intero.")
        if danno < 0:
            raise ValueError("danno non può essere negativo.")
        danno_effettivo = max(0, danno)
        self.__vita = max(0, self.__vita - danno_effettivo)
        return danno_effettivo
    
    #Funzione che gestisce l'attacco di un personaggio verso un altro
    def attacca(self, nemico: "Personaggio") -> int:
        #Se non ha un'arma equipaggiata, danno base = 1
        if not self.__arma:
            danno = 1
        else:
            danno = self.__arma.get_danno()
        
        nemico.subisci(danno)
        return danno

    #Funzione che aggiunge una pozione all'inventario
    def aggiungi_pozione(self, pozione):
        self.__pozioni.append(pozione)

    #Funzione che decide se usare una pozione
    def scegli_se_usare_la_pozione(self, nemico):
        if not self.__pozioni:
            return None
        
        if self.__vita < self.__vita_massima * 0.4:
            for pozione in self.__pozioni:
                if pozione.effetto == "cura":
                    return pozione
        
        if nemico.vita > nemico.vita_massima * 0.6:
            for pozione in self.__pozioni:
                if pozione.effetto in ["buff_forza", "buff_destrezza"]:
                    return pozione
        
        return None

    #Funzione che usa una pozione
    def usa_pozione(self, pozione):
        pozione.applica_a(self)
        self.__pozioni.remove(pozione)

    #Funzione che aggiunge un buff temporaneo a una caratteristica
    def aggiungi_buff(self, caratteristica: str, quantita: int, durata: int) -> None:
        if caratteristica == "forza":
            self.__forza += quantita
        elif caratteristica == "destrezza":
            self.__destrezza += quantita

    #Funzione che guarisce il personaggio
    def guarisci(self, quantita: int) -> int:
        #Validazioni:
        #1)Solleva TypeError se quantita non è intero
        #2)Solleva ValueError se quantita è negativa
        if not isinstance(quantita, int):
            raise TypeError("quantita deve essere un intero.")
        if quantita < 0:
            raise ValueError("quantita non può essere negativa.")
        guarigione = min(quantita, self.__vita_massima - self.__vita)
        self.__vita += guarigione
        return guarigione

    #Funzione che aggiorna i buff
    def controllo_buff(self):
        pass

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
        self.__vita = vita

    #Imposto le "property" (getter e setter) per la vita_massima 
    @property
    def vita_massima(self):
        return self.__vita_massima

    @vita_massima.setter
    def vita_massima(self, vita_massima: int):
        self.__vita_massima = vita_massima

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
        #Controllo duck-typing sull'oggetto arma:
        #1)Solleva TypeError se l'oggetto non ha i metodi/attributi attesi
        if arma is not None and not (hasattr(arma, "get_danno") and (hasattr(arma, "tipo") or hasattr(arma, "get_type"))):
            raise TypeError("Oggetto non equipaggiabile, non è un’arma valida.")
        self.__arma = arma

    def __str__(self):
        return f"{self.__nome}: {self.__vita}/{self.__vita_massima} HP"