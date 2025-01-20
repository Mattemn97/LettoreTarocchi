import random
import json

def stesa_celtica_semplice(file_json):
    print("Stesa Croce Celtica semplice")
    try:
        """Estrae 8 carte da un mazzo di tarocchi definito in un file JSON."""
        # Caricamento del mazzo di carte dal file JSON
        with open(file_json, 'r', encoding='utf-8') as file:
            mazzo = json.load(file)

        # Mescolamento del mazzo
        random.shuffle(mazzo)

        # Estrazione di 8 carte
        carte_estratte = random.sample(mazzo, 8)

        # Stampa le carte estratte
        print(f"Sinistra: {carte_estratte[0]['Titolo']} - {carte_estratte[0]['BreveDescrizione']}")
        print(f"Centro: {carte_estratte[1]['Titolo']} - {carte_estratte[1]['BreveDescrizione']}")
        print(f"Destra: {carte_estratte[2]['Titolo']} - {carte_estratte[2]['BreveDescrizione']}")
        print(f"Alto: {carte_estratte[3]['Titolo']} - {carte_estratte[3]['BreveDescrizione']}")
        print(f"Basso: {carte_estratte[4]['Titolo']} - {carte_estratte[4]['BreveDescrizione']}")

        print(f"Fondo mazzo 1: {carte_estratte[5]['Titolo']} - {carte_estratte[5]['BreveDescrizione']}")
        print(f"Fondo mazzo 2: {carte_estratte[6]['Titolo']} - {carte_estratte[6]['BreveDescrizione']}")
        print(f"Fondo mazzo 3: {carte_estratte[7]['Titolo']} - {carte_estratte[7]['BreveDescrizione']}")

        print("-" * 40)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")