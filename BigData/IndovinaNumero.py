import random
x = random.randint(1, 10)
n = int(input("Indovina il numero: "))
while n != x:
    if n < x:
        print("Troppo basso!")
    else:
        print("Troppo alto!")
    n = int(input("Sbagliato, riprova: "))
print("Bravo, hai indovinato!")