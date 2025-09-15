"""
Chiedete all'utente un elenco di numeri
Restituisci la media di tutti i numeri 
"""

def call_media():
    somma = 0
    numeri = 0
    while True:
        x = input("Inserisci numero: ")
        # numeri +=1
        if(x == ""):
            break
        numeri+=1
        somma += int(x)
    return int(somma / numeri)

print(call_media())