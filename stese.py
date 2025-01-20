import random
import json

def menu_stesa(file_json):
    while True:
        # Stampa del menu
        print("1. Stesa del futuro")
        print("2. Opzione 2")
        print("3. Opzione 3")
        print("4. Esci")
        
    
        # Richiesta di input
        scelta = input("Scegli una stesa: ")
        
        if scelta == '1':
            menu_metodi_futuro(file_json)
            break
        elif scelta == '2':
            print("Non implementata per ora...")
            break
        elif scelta == '3':
            print("Non implementata per ora...")
            break
        elif scelta == '4':
            print("Uscita...")
            break

        else:
            print("Scelta non valida. Riprova.")

def menu_metodi_futuro(file_json):
    while True:
        # Stampa del menu
        print("1. Metodo croce celtica semplice")
        print("2. Metodo croce celtica completa")
        print("3. Opzione 3")
        print("4. Esci")
        
        # Richiesta di input
        scelta = input("Scegli un metodo: ")
        
        if scelta == '1':
            metodo_celtica_semplice(file_json)
            break
        elif scelta == '2':
            metodo_celtica_completa(file_json)
            break
        elif scelta == '3':
            print("Non implementata per ora...")
            break
        elif scelta == '4':
            print("Uscita...")
            break
        else:
            print("Scelta non valida. Riprova.")

def metodo_celtica_semplice(file_json):
    print("-" * 40)
    print("Metodo Croce Celtica semplice")
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_json, 'r', encoding='utf-8') as file:
            mazzo = json.load(file)

        # Mescolamento del mazzo
        random.shuffle(mazzo)

        # Estrazione di 8 carte
        carte_estratte = random.sample(mazzo, 8)

        # Stampa le carte estratte
        print(f"Influenze passate: {carte_estratte[0]['Titolo']} - {carte_estratte[0]['BreveDescrizione']}")
        print(f"Influenze attuali: {carte_estratte[1]['Titolo']} - {carte_estratte[1]['BreveDescrizione']}")
        print(f"Influenze future: {carte_estratte[2]['Titolo']} - {carte_estratte[2]['BreveDescrizione']}")
        print(f"Influenze esterne: {carte_estratte[3]['Titolo']} - {carte_estratte[3]['BreveDescrizione']}")
        print(f"Influenze interne: {carte_estratte[4]['Titolo']} - {carte_estratte[4]['BreveDescrizione']}")

        print(f"Fondo mazzo 1: {carte_estratte[5]['Titolo']} - {carte_estratte[5]['BreveDescrizione']}")
        print(f"Fondo mazzo 2: {carte_estratte[6]['Titolo']} - {carte_estratte[6]['BreveDescrizione']}")
        print(f"Fondo mazzo 3: {carte_estratte[7]['Titolo']} - {carte_estratte[7]['BreveDescrizione']}")

        print("-" * 40)
    
    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")

def metodo_celtica_completa(file_json):
    print("-" * 40)
    print("Metodo Croce Celtica completa")
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_json, 'r', encoding='utf-8') as file:
            mazzo = json.load(file)

        # Mescolamento del mazzo
        random.shuffle(mazzo)

        # Estrazione di 8 carte
        carte_estratte = random.sample(mazzo, 10)

        # Stampa le carte estratte
        print(f"Ciò che sta accadendo: {carte_estratte[0]['Titolo']} - {carte_estratte[0]['BreveDescrizione']}")
        print(f"Influenze esterne: {carte_estratte[1]['Titolo']} - {carte_estratte[1]['BreveDescrizione']}")
        print(f"Riflessioni: {carte_estratte[2]['Titolo']} - {carte_estratte[2]['BreveDescrizione']}")
        print(f"Sentimenti: {carte_estratte[3]['Titolo']} - {carte_estratte[3]['BreveDescrizione']}")
        print(f"La vera causa: {carte_estratte[4]['Titolo']} - {carte_estratte[4]['BreveDescrizione']}")
        print(f"Sviluppo situazione: {carte_estratte[5]['Titolo']} - {carte_estratte[5]['BreveDescrizione']}")
        print(f"Ciò che si vuole ottenere: {carte_estratte[6]['Titolo']} - {carte_estratte[6]['BreveDescrizione']}")
        print(f"Il punto di vista degli altri: {carte_estratte[7]['Titolo']} - {carte_estratte[7]['BreveDescrizione']}")
        print(f"Speranze o paure: {carte_estratte[8]['Titolo']} - {carte_estratte[8]['BreveDescrizione']}")
        print(f"Risultato nel lontano futuro: {carte_estratte[9]['Titolo']} - {carte_estratte[9]['BreveDescrizione']}")

        print("-" * 40)
    
    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")