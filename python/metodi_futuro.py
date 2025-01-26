import json

import utility

file_mazzo = "mazzo_tarocchi.json" 
file_descrizione_medodi = "descrizione_metodi_futuro.json"

def menu_metodi():
    print("- " * 20)
    global file_mazzo
    global file_descrizione_medodi
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_descrizione_medodi, 'r', encoding='utf-8') as file:
            descr_metodi = json.load(file)
        
        # Stampa del menu
        while True:
            for metodo in descr_metodi:
                print(f"{metodo['Identificativo']}. {metodo['Titolo']}")
            
            scelta = int(input("Scegli un metodo: "))

            for metodo in descr_metodi:
                if metodo['Identificativo'] == scelta:
                    exec(metodo['Funzione'])
            break

    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")

def metodo_celtica_semplice(file_json):
    print("- " * 20)
    print("Metodo croce celtica semplice")
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_json, 'r', encoding='utf-8') as file:
            mazzo = json.load(file)
        
            carte_estratte = utility.pesca_tot_carte(mazzo, 8)

        # Stampa le carte estratte
        print(f"Influenze passate:")
        utility.stampa_carta(carte_estratte[0], True)
        print(f"\nInfluenze attuali:")
        utility.stampa_carta(carte_estratte[1], True)
        print(f"\nInfluenze future:")
        utility.stampa_carta(carte_estratte[2], True)
        print(f"\nInfluenze esterne:")
        utility.stampa_carta(carte_estratte[3], True)
        print(f"\nInfluenze interne:")
        utility.stampa_carta(carte_estratte[4], True)
        print(f"\nFondo mazzo 1:")
        utility.stampa_carta(carte_estratte[5], True)
        print(f"\nFondo mazzo 2:")
        utility.stampa_carta(carte_estratte[6], True)
        print(f"\nFonod mazzo 3:")
        utility.stampa_carta(carte_estratte[7], True)

    
    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")

def metodo_celtica_completa(file_json):
    print("- " * 20)
    print("Metodo croce celtica completa")
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_json, 'r', encoding='utf-8') as file:
            mazzo = json.load(file)

            carte_estratte = utility.pesca_tot_carte(mazzo, 10)

        # Stampa le carte estratte
        print(f"Ciò che sta accadendo:")
        utility.stampa_carta(carte_estratte[0], True)
        print(f"\nInfluenze esterne:")
        utility.stampa_carta(carte_estratte[1], True)
        print(f"\nRiflessioni:")
        utility.stampa_carta(carte_estratte[2], True)
        print(f"\nSentimenti:")
        utility.stampa_carta(carte_estratte[3], True)
        print(f"\nLa vera causa:")
        utility.stampa_carta(carte_estratte[4], True)
        print(f"\nSviluppo situazione:")
        utility.stampa_carta(carte_estratte[5], True)
        print(f"\nCiò che si vuole ottenere:")
        utility.stampa_carta(carte_estratte[6], True)
        print(f"\nIl punto di vista degli altri:")
        utility.stampa_carta(carte_estratte[7], True)
        print(f"\nSperanze o paure:")
        utility.stampa_carta(carte_estratte[8], True)
        print(f"\nRisultato nel lontano futuro:")
        utility.stampa_carta(carte_estratte[9], True)
    
    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")

def metodo_singola_carta(file_json):
    print("- " * 20)
    print("Metodo singola carta")
    try:
        # Caricamento del mazzo di carte dal file JSON
        with open(file_json, 'r', encoding='utf-8') as file:
            mazzo = json.load(file)

            carte_estratte = utility.pesca_tot_carte(mazzo, 1)

        # Stampa le carte estratte
        print(f"Carta estratta:")
        utility.stampa_carta(carte_estratte[0], True)

    # Gestione eventuali errori
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore: Il file JSON non esiste o non è valido.")
    except ValueError as e:
        print(f"Errore: {e}")
