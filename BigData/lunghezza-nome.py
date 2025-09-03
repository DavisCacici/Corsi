# Richiedere all'utente il nome e il cognome con un solo input, 
# una volta ricevuti andare a rimuovere gli spazi dalla stringa ricevuta e separare i vari elementi
# infine dare in output la lunghezza singola di ogni elemento e quella totale

x = input("Qual è il tuo nome e cognome: ")
y=""
tot=0
myList=[]
for i in range(0,len(x)):
    if(x[i]==" "):
        myList.append(y)
        y=""
    else:
        y+=x[i]
myList.append(y)
print(myList)
for i in range(0,len(myList)):
    tot+=len(myList[i])
    print("Il tuo nome è lungo:", len(myList[i]))
print("in totale il tuo nome è lungo:", tot)
    