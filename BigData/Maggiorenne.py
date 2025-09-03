u = int(input("Quanti anni hai? "))
if u >= 0:
    if u >= 18:
        print("Sei maggiorenne")
    else:
        print("Sei minorenne")
else:
    print("Errore: età non valida")