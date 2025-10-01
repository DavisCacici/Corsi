import numpy

file = open("..\\dati\\bi.csv", "r")
for i in file.readlines():
    print(i)
file.close()