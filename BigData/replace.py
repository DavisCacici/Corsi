"""
Chiedere all'utente 3 cose:
    - La stringa in analisi
    - Il carattere da sostituire
    - Il carattere con quale sostituirlo

Processo:
    Cercare nella stringa in analisi il carattere da sostituire e rimpiazzarlo 
    con quello nuovo
"""
import new_method
p1 = input("Stringa in analisi: ")
p2 = input("Carattere da sostituire: ")
p3 = input("Nuovo carattere: ")




pippo = new_method.new_replace(p1, p2, p3)

print(pippo)