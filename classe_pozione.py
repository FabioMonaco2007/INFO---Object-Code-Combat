class Pozione:
    def __init__(self, nome: str, effetto: str, quantita: int, durata: int = 0):
        self.__nome = nome
        self.__effetto = effetto
        self.__quantita = quantita
        self.__durata = durata
        self.__usata = False

    #Imposto la "property" (getter) per il nome 
    @property
    def nome(self):
        return self.__nome

    #Imposto la "property" (getter) per l'effetto 
    @property
    def effetto(self):
        return self.__effetto

    #Imposto la "property" (getter) per la quantita 
    @property
    def quantita(self):
        return self.__quantita

    #Imposto la "property" (getter) per la durata 
    @property
    def durata(self):
        return self.__durata

    #Funzione che applica l'effetto della pozione al bersaglio
    def applica_a(self, bersaglio):
        if self.__usata:
            print("Errore: questa pozione è già stata consumata!")
            return

        if self.__effetto == "cura":
            if not hasattr(bersaglio, 'guarisci') or not callable(getattr(bersaglio, 'guarisci')):
                print("Errore: il bersaglio non supporta 'guarisci'")
                return
            bersaglio.guarisci(self.__quantita)
        else:
            if not hasattr(bersaglio, 'aggiungi_buff') or not callable(getattr(bersaglio, 'aggiungi_buff')):
                print("Errore: il bersaglio non supporta 'aggiungi_buff'")
                return
            caratteristica = "forza" if self.__effetto == "buff_forza" else "destrezza"
            bersaglio.aggiungi_buff(caratteristica, self.__quantita, self.__durata)

        self.__usata = True

    #Funzione che fornisce una descrizione della pozione
    def __str__(self):
        if self.__effetto == "cura":
            return f"Pozione({self.__effetto} +{self.__quantita})"
        else:
            return f"Pozione({self.__effetto} +{self.__quantita} x{self.__durata}t)"