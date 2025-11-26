from classe_carta import Carta
from classe_mazzo import Mazzo
from classe_mano import Mano

if __name__ == "__main__":
    semi = ['♠', '♥', '♦', '♣']
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    carte = [Carta(seme, valore) for seme in semi for valore in valori]

    mazzo = Mazzo(carte)
    mazzo.mescola()

    mano = Mano()
    for _ in range(5):
        mano.aggiungi_carta(mazzo.pesca())
        
    print("Le tue 5 carte sono:")
    print(mano)