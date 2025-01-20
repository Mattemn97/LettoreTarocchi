import random
import json

def estrai_carte(file_json):
    """Estrae 8 carte da un mazzo di tarocchi definito in un file JSON."""
    # Caricamento del mazzo di carte dal file JSON
    with open(file_json, 'r', encoding='utf-8') as file:
        mazzo = json.load(file)

    # Controllo che il mazzo contenga carte valide
    if len(mazzo) < 8:
        raise ValueError("Il mazzo deve contenere almeno 8 carte.")

    # Mescolamento del mazzo
    random.shuffle(mazzo)

    # Estrazione di 8 carte
    carte_estratte = random.sample(mazzo, 8)

    return carte_estratte

def stampa_carte(carte):
    """Stampa i dettagli delle carte estratte."""
    for carta in carte:
        print(f"Titolo: {carta['titolo']}")
        print(f"Breve introduzione: {carta['breve introduzione']}")
        print(f"Numerologia: {carta['numerologia']}")
        print(f"Elementi: {carta['elementi']}")
        print(f"Lettura: {carta['lettura']}")
        print(f"Chakra: {carta['Chakra']}")
        print(f"Pianeta/Oroscopo: {carta['Pianeta-oroscopo']}")
        print(f"Significato: {carta['Significato']}")
        print(f"Significato inverso: {carta['significato inverso']}")
        print("-" * 40)

if __name__ == "__main__":
    file_mazzo = "mazzo_tarocchi.json"  # Nome del file JSON contenente il mazzo di tarocchi
    try:
        carte = estrai_carte(file_mazzo)
        print("Le 8 carte estratte sono:")
        stampa_carte(carte)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")