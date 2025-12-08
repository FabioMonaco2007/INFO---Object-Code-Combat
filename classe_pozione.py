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
        #Validazioni e controlli:
        #Solleva ValueError se la pozione è già stata consumata
        #1)Per 'cura': solleva TypeError se il bersaglio non supporta 'guarisci'
        #              solleva ValueError se il bersaglio ha già HP massimi
        #2)Per 'buff_*': solleva TypeError se il bersaglio non supporta 'aggiungi_buff'
        #                solleva ValueError se il buff relativo è già attivo (se rilevabile)
        if self.__usata:
            raise ValueError("Errore: questa pozione è già stata consumata!")

        if self.__effetto == "cura":
            if not hasattr(bersaglio, 'guarisci') or not callable(getattr(bersaglio, 'guarisci')):
                raise TypeError("Errore: il bersaglio non supporta 'guarisci'")
            #Assume proprietà 'vita' e 'vita_massima' per il bersaglio
            if hasattr(bersaglio, 'vita') and hasattr(bersaglio, 'vita_massima'):
                if bersaglio.vita >= bersaglio.vita_massima:
                    raise ValueError("Il bersaglio ha già HP massimi.")
            bersaglio.guarisci(self.__quantita)
        else:
            if not hasattr(bersaglio, 'aggiungi_buff') or not callable(getattr(bersaglio, 'aggiungi_buff')):
                raise TypeError("Errore: il bersaglio non supporta 'aggiungi_buff'")
            caratteristica = "forza" if self.__effetto == "buff_forza" else "destrezza"
            #Se il bersaglio espone una struttura 'buffs' si controlla se il buff è già attivo
            if hasattr(bersaglio, 'buffs'):
                try:
                    buffs = getattr(bersaglio, 'buffs')
                    if isinstance(buffs, dict) and buffs.get(caratteristica):
                        raise ValueError(f"Buff alla {caratteristica} già attivo")
                except Exception:
                    #Se la struttura non è controllabile, procediamo comunque ad applicare il buff
                    pass
            bersaglio.aggiungi_buff(caratteristica, self.__quantita, self.__durata)

        self.__usata = True

    #Funzione che fornisce una descrizione della pozione
    def __str__(self):
        if self.__effetto == "cura":
            return f"Pozione({self.__effetto} +{self.__quantita})"
        else:
            return f"Pozione({self.__effetto} +{self.__quantita} x{self.__durata}t)"