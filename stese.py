import random
import json

import stese_futuro

file_descrizione_stese = "descrizione_stese.json"

def menu_stesa():
    global file_descrizione_stese
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_descrizione_stese, 'r', encoding='utf-8') as file:
            descr_stese = json.load(file)
        
        # Stampa del menu
        while True:
            for stesa in descr_stese:
                print(f"ID {stesa['Identificativo']}. {stesa['Titolo']}")
            
            scelta = int(input("Scegli una stesa: "))

            for stesa in descr_stese:
                if stesa['Identificativo'] == scelta:
                    exec(stesa['Funzione'])
            break

    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")
