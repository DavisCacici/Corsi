# f = open("C:\\_SORGENTI\\Corsi\\BigData\\dati\\bi.csv", "rt")
# print(f.read())
# f.close()

with open("..\\dati\\bi.csv") as file:
    print(file.read())