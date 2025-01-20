import random
import json

def estrai_carte(file_json):
    """Estrae 8 carte da un mazzo di 52 carte definito in un file JSON."""
    # Caricamento del mazzo di carte dal file JSON
    with open(file_json, 'r') as file:
        mazzo = json.load(file)

    # Controllo che il mazzo contenga esattamente 52 carte
    if len(mazzo) != 52:
        raise ValueError("Il mazzo deve contenere esattamente 52 carte.")

    # Mescolamento del mazzo
    random.shuffle(mazzo)

    # Estrazione di 8 carte
    carte_estratte = random.sample(mazzo, 8)

    return carte_estratte

if __name__ == "__main__":
    file_mazzo = "mazzo.json"  # Nome del file JSON contenente il mazzo di carte
    try:
        carte = estrai_carte(file_mazzo)
        print("Le 8 carte estratte sono:")
        for carta in carte:
            print(carta)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")