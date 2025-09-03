"""
Chiedete all'utente un elenco di numeri
Restituisci la somma di tutti i numeri 
"""

x = int(input("Quanti numeri vuoi aggiungere? "))
somma = 0
for i in range(0, x):
    somma += int(input("Inserisci numero: "))
    
print("La somma è:", somma)