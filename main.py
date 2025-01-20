import stese

def stampa_carte(carte):
    """Stampa i dettagli delle carte estratte."""
    for carta in carte:
        print(f"Titolo: {carta['Titolo']}")
        print(f"BreveDescrizione: {carta['BreveDescrizione']}")
        print(f"Numerologia: {carta['Numerologia']}")
        print(f"Elementi: {carta['Elementi']}")
        print(f"Lettura: {carta['Lettura']}")
        print(f"Chakra: {carta['Chakra']}")
        print(f"PianetaOroscopo: {carta['PianetaOroscopo']}")
        print(f"Significato: {carta['Significato']}")
        print(f"SignificatoInverso: {carta['SignificatoInverso']}")
        print("-" * 40)

if __name__ == "__main__":
    # Nome del file JSON contenente il mazzo di tarocchi
    file_mazzo = "mazzo_tarocchi.json"  
    # Implementare menù gestione stese
    stese.stesa_celtica_semplice(file_mazzo)
    