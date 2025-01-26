import random

def stampa_carta(carta, inverso):
    if not inverso:
        print(f"{carta['Titolo']} - {carta['BreveDescrizione']}\n\t{carta['Significato']}")
    else:
        devio = random.randint(0,1)
        if devio:
            print(f"{carta['Titolo']} - {carta['BreveDescrizione']}\n\tSignificato: {carta['Significato']}")
        else:
            print(f"{carta['Titolo']} - {carta['BreveDescrizione']}\n\tSignificato inverso: {carta['SignificatoInverso']}")


def pesca_tot_carte(mazzo, tot):
    random.shuffle(mazzo)
    carte_estratte = random.sample(mazzo, tot)

    return carte_estratte