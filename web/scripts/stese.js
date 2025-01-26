async function menuStesa(fileDescrizioneStese) {
    try {
      const descrStese = await caricaJson(fileDescrizioneStese);
  
      // Crea un menu con le stese disponibili
      const menuDiv = document.getElementById("stese-list");
      menuDiv.innerHTML = "";
  
      descrStese.forEach((stesa) => {
        const button = document.createElement("button");
        button.textContent = `${stesa.Identificativo}. ${stesa.Titolo}`;
        button.addEventListener("click", () => {
          eseguiStesa(stesa.Funzione);
        });
        menuDiv.appendChild(button);
      });
    } catch (error) {
      console.error("Errore:", error);
      alert("Errore nel caricamento delle stese.");
    }
  }
  
  function eseguiStesa(funzione) {
    const resultDiv = document.getElementById("result");
    resultDiv.textContent = "";
  
    if (funzione === "metodoCelticaSemplice") {
      metodoCelticaSemplice("mazzo_tarocchi.json").then((risultati) => {
        resultDiv.textContent = risultati;
      });
    } else {
      resultDiv.textContent = "Funzione non ancora implementata.";
    }
  }
  