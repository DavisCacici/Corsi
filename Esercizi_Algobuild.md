## Esercizi AlgoBuild
Ecco 10 esercizi per principianti utilizzando Algobuild, con input, output e processo descritti in dettaglio:

**Esercizio 1:** Somma di due numeri  
- **Input:** Due numeri interi inseriti dall'utente.  
- **Output:** La somma dei due numeri.  
- **Processo:**  
  1. Leggi il primo numero (es. `a`).  
  2. Leggi il secondo numero (es. `b`).  
  3. Calcola `risultato = a + b`.  
  4. Stampa `risultato`.  

**Esercizio 2:** Controllo pari o dispari  
- **Input:** Un numero intero.  
- **Output:** "Pari" se il numero è pari, altrimenti "Dispari".  
- **Processo:**  
  1. Leggi il numero (es. `n`).  
  2. Se `n % 2 == 0`, stampa "Pari".  
  3. Altrimenti, stampa "Dispari".  

**Esercizio 3:** Area di un rettangolo  
- **Input:** Base e altezza (due numeri decimali).  
- **Output:** L'area del rettangolo.  
- **Processo:**  
  1. Leggi `base` e `altezza`.  
  2. Calcola `area = base * altezza`.  
  3. Stampa `area`.  

**Esercizio 4:** Maggiore tra due numeri  
- **Input:** Due numeri interi.  
- **Output:** Il numero maggiore.  
- **Processo:**  
  1. Leggi `num1` e `num2`.  
  2. Se `num1 > num2`, stampa `num1`.  
  3. Altrimenti, stampa `num2`.  

**Esercizio 5:** Conversione Celsius → Fahrenheit  
- **Input:** Temperatura in gradi Celsius.  
- **Output:** Temperatura in Fahrenheit.  
- **Processo:**  
  1. Leggi `celsius`.  
  2. Calcola `fahrenheit = (celsius * 9/5) + 32`.  
  3. Stampa `fahrenheit`.  

**Esercizio 6:** Contatore di lettere in una parola  
- **Input:** Una parola (stringa).  
- **Output:** Il numero di caratteri della parola.  
- **Processo:**  
  1. Leggi `parola`.  
  2. Calcola `lunghezza = lunghezza_di(parola)`.  
  3. Stampa `lunghezza`.  

**Esercizio 7:** Somma dei primi N numeri naturali  
- **Input:** Un numero intero positivo `N`.  
- **Output:** Somma dei primi `N` numeri naturali.  
- **Processo:**  
  1. Leggi `N`.  
  2. Inizializza `somma = 0` e `contatore = 1`.  
  3. Ripeti finché `contatore <= N`:  
     - `somma = somma + contatore`  
     - `contatore = contatore + 1`  
  4. Stampa `somma`.  

**Esercizio 8:** Verifica vocale/consonante  
- **Input:** Un carattere (lettera).  
- **Output:** "Vocale" o "Consonante".  
- **Processo:**  
  1. Leggi `carattere`.  
  2. Se `carattere` è una di `a, e, i, o, u`, stampa "Vocale".  
  3. Altrimenti, stampa "Consonante".  

**Esercizio 9:** Calcolo dell'età  
- **Input:** Anno di nascita e anno corrente.  
- **Output:** Età della persona.  
- **Processo:**  
  1. Leggi `anno_nascita` e `anno_corrente`.  
  2. Calcola `età = anno_corrente - anno_nascita`.  
  3. Stampa `età`.  

**Esercizio 10:** Inversione di una stringa  
- **Input:** Una stringa (es. "ciao").  
- **Output:** La stringa invertita (es. "oaic").  
- **Processo:**  
  1. Leggi `stringa`.  
  2. Inizializza `stringa_invertita` come stringa vuota.  
  3. Per ogni carattere in `stringa` (partendo dalla fine):  
     - Aggiungi il carattere a `stringa_invertita`.  
  4. Stampa `stringa_invertita`.  

________________________________________

**Esercizio 1:** Classificatore di triangoli
- **Input:** Tre numeri (lati del triangolo)
- **Output:** Tipo di triangolo (Equilatero, Isoscele, Scaleno o Non valido)
- **Processo:**
    1.	Leggi i tre lati (a, b, c)
    2.	Se a + b > c E b + c > a E a + c > b:
        - Se a = b E b = c → "Equilatero"
        - Altrimenti se a = b O b = c O a = c → "Isoscele"
        - Altrimenti → "Scaleno"
    3.	Altrimenti → "Non valido"

**Esercizio 2:** Calcolatore di sconti
- **Input:** Prezzo originale e categoria cliente (Standard, Premium, VIP)
- **Output:** Prezzo scontato
- **Processo:**
    1.	Leggi prezzo e categoria
    2.	Se categoria = "Premium":
        - Se prezzo > 100 → sconto 20%
        - Altrimenti → sconto 10%
    3.	Se categoria = "VIP":
        - Se prezzo > 200 → sconto 30%
        - Altrimenti → sconto 15%
    4.	Altrimenti:
        - Se prezzo > 50 → sconto 5%
        - Altrimenti → nessuno sconto
    5.	Calcola prezzo scontato

**Esercizio 3:** Giudizio voto esame
- **Input:** Voto numerico (0-30)
- **Output:** Giudizio (Insufficiente, Sufficiente, Buono, Ottimo)
- **Processo:**
    1.	Leggi voto
    2.	Se voto < 18 → "Insufficiente"
    3.	Altrimenti se voto ≤ 22 → "Sufficiente"
    4.	Altrimenti se voto ≤ 27 → "Buono"
    5.	Altrimenti → "Ottimo"

**Esercizio 4:** Controllo accessi con orario
- **Input:** Età, tipo biglietto (Intero/Ridotto), orario corrente (hh:mm)
- **Output:** "Accesso consentito" o "Accesso negato"
- **Processo:**
    1.	Leggi età, biglietto, orario
    2.	Se orario < 18:00:
        - Se età ≥ 14 O biglietto = "Ridotto" → "Accesso consentito"
        - Altrimenti → "Accesso negato"
    3.	Altrimenti:
        - Se età ≥ 18 → "Accesso consentito"
        - Altrimenti → "Accesso negato"

**Esercizio 5:** Calcolo imposte progressive
- **Input:** Reddito annuale
- **Output:** Importo tasse da pagare
- **Processo:**
    1.	Leggi reddito
    2.	Se reddito ≤ 15000 → tasse = reddito × 10%
    3.	Altrimenti se reddito ≤ 28000:
    - tasse = 1500 + (reddito - 15000) × 15%
    4.	Altrimenti se reddito ≤ 50000:
        - tasse = 3450 + (reddito - 28000) × 25%
    5.	Altrimenti:
        - tasse = 8950 + (reddito - 50000) × 35%
    6.	Stampa tasse

