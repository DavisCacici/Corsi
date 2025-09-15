"""
Avendo 2 numeri in input scopri qual è il loro rapporto:
    - se n1 è maggiore di n2
    - se n1 è uguale di n2
    - se n1 è minore di n2
"""

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

if n1 > n2:
    print(n1, "è maggiore di", n2)
elif n1 < n2:
    print(n1, "è minore di", n2)
else:
    print(n1, "è uguale a", n2)
