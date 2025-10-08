# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
    nome = "Stefano"
    cognome = "Rossi"
    
#--------------------------------------------------------
persona = Person()
persona2 = Person()
persona3 = Person()
print(persona)
print(persona.nome)
print(persona.cognome)
print(persona2.nome)
print(persona2.cognome)
print(persona3.nome)
print(persona3.cognome)