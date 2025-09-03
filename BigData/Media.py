"""
Chiedete all'utente un elenco di numeri
Restituisci la media di tutti i numeri 
"""
somma = 0
numeri = 0
while True:
    x = input("Inserisci numero: ")
    # numeri +=1
    if(x == ""):
        break
    
    somma += int(x)
print(somma)