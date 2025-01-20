import random

def estrai_carte():
    """Estrae 8 carte da un mazzo di 52 carte."""
    # Definizione del mazzo di carte
    semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Creazione del mazzo completo
    mazzo = [f"{valore} di {seme}" for valore in valori for seme in semi]

    # Mescolamento del mazzo
    random.shuffle(mazzo)

    # Estrazione di 8 carte
    carte_estratte = random.sample(mazzo, 8)

    return carte_estratte

if __name__ == "__main__":
    carte = estrai_carte()
    print("Le 8 carte estratte sono:")
    for carta in carte:
        print(carta)
