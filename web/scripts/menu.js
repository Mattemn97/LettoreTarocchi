// Funzione per caricare il contenuto dinamico della pagina
function caricaMenuPrincipale() {
    const container = document.getElementById("container");
    container.innerHTML = `
        <h1>Menu principale</h1>
        <p>Scegli un'opzione dal menu:</p>
        <button onclick="apriMenuStese()">Gestione Stese</button>
        <button onclick="apriMenuMetodi()">Gestione Metodi Futuri</button>
    `;
}

// Funzione per aprire il menu delle stese
function apriMenuStese() {
    const container = document.getElementById("container");
    container.innerHTML = `
        <h1>Gestione Stese</h1>
        <p>Seleziona una stesa da eseguire:</p>
        <div id="menuStese"></div>
        <button onclick="caricaMenuPrincipale()">Torna al menu principale</button>
    `;
    caricaStese();
}

// Funzione per aprire il menu dei metodi futuri
function apriMenuMetodi() {
    const container = document.getElementById("container");
    container.innerHTML = `
        <h1>Gestione Metodi Futuri</h1>
        <p>Seleziona un metodo da eseguire:</p>
        <div id="menuMetodi"></div>
        <button onclick="caricaMenuPrincipale()">Torna al menu principale</button>
    `;
    caricaMetodi();
}

// Funzione per caricare le stese dal file JSON
async function caricaStese() {
    try {
        const response = await fetch("descrizione_stese.json");
        const descrizioneStese = await response.json();

        const menuStese = document.getElementById("menuStese");
        descrizioneStese.forEach((stesa) => {
            const button = document.createElement("button");
            button.textContent = `${stesa.Identificativo}. ${stesa.Titolo}`;
            button.onclick = () => eval(stesa.Funzione); // Esegui la funzione specificata
            menuStese.appendChild(button);
        });
    } catch (error) {
        console.error("Errore nel caricamento delle stese:", error);
    }
}

// Funzione per caricare i metodi futuri dal file JSON
async function caricaMetodi() {
    try {
        const response = await fetch("descrizione_metodi_futuro.json");
        const descrizioneMetodi = await response.json();

        const menuMetodi = document.getElementById("menuMetodi");
        descrizioneMetodi.forEach((metodo) => {
            const button = document.createElement("button");
            button.textContent = `${metodo.Identificativo}. ${metodo.Titolo}`;
            button.onclick = () => eval(metodo.Funzione); // Esegui la funzione specificata
            menuMetodi.appendChild(button);
        });
    } catch (error) {
        console.error("Errore nel caricamento dei metodi futuri:", error);
    }
}

// Carica il menu principale al caricamento della pagina
document.addEventListener("DOMContentLoaded", caricaMenuPrincipale);
