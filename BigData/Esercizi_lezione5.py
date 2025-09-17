#Esercizio n°1
"""
Completa la funzione square_sum che eleva al quadrato 
tutti gli elementi nell'array e 
li somma tra di loro per ottenere il risultato.

Per esempio, per [1, 2, 2] dovrebbe ritornare 9  

def square_sum(numbers: List[int]) -> int:
    pass

"""

#Esercizio n°2
"""
Avendo una lista o un stringa in input, crea la funzione next_item che:
-   input:
    -   lista o stringa
    -   Elemento dalla quale partire per cercare il suo successivo
-   output:
    -   Se dovesse essere l'ultimo elemento o non dovesse trovarsi 
        nella lista ritornare None

next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally" 
next_item(['Joe', 'Bob', 'Sally'], 'Sally') # => None 
next_item('testing', 't') # => 'e'
next_item('testing', 'a') # => None

def next_item(array: Any, item: Any) -> Any:
    pass
"""

#Esercizio n°3
"""
Risolvi il problema della funzione seguente.
Questa funzione semplicemente ritorna una risposta in base all'input, 
se le viene passato 42 ritorna "everything", se gli viene passato 42 * 42 ritorna 'everything squared'
altrimenti ritorna 'nothing', ma in questa funzione c'è un errore risolvilo

def what_is(x: int) -> str:
    if x is 42:
        return 'everything'
    elif x is 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'
"""

#Esercizio n°4
"""
Avendo un disordinato array di 3 interi positivi [n1, n2, n3], determina se è possibile formare 
una terna pitagorica usando questi 3 interi con la seguente formula
a2 + b2 = c2

Ritorna True o False se è possibile o meno

def pythagorean_triple(integers: List[int]) -> bool:
    pass
"""

#Esercizio n°5
"""
Avendo una stringa di lunghezza arbitraria con qualsiasi carattere ascii
Scrivi una funzione che determini se la stringa contiente l'intera parola 'English'.
L'ordine dei carattere è importante -- una stringa "abcEnglishdef" è corretta ma "abcnEglishsef" non lo è.
Maiuscolo o minuscole non importa -- "eNglisH" è comunque corretto.

def sp_eng(sentence: str) -> bool:
    pass
"""

#Esercizio n°6
"""
Avendo un numero in input moltiplicalo per 8 se positivo
se negativo moltiplicalo per 9

def simple_multiplication(number: int) -> int:
    pass
"""

#Esercizio n°7
"""
Considera una array/list di percore dove 
alcune pecore potrebbero essere perse. 
Abbiamo bisogno di una funzione che conta in numero di pecore presenti nell'array/list (True significa presente).
Per esempio:
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

La risposta corretta è 17

def count_sheeps(array_of_sheep: List[bool]) -> int:
    pass
"""

#Esercizio n°8
"""
Scrivi una funzione che accetti un numero intero non negativo n e una stringa s come parametri,
e ritorna una stringa di s ripetuta esattamente n volte

Esempio:

6, "I"      -> "IIIIII"
5, "Hello"  -> "HelloHelloHelloHelloHello"

def repeat_str(repeat: int, string: str) -> str:
    pass
"""

#Esercizio n°9
"""
Scrivi un programma che trovi la somma di ogni numero da 1 a num (entrambi inclusi). 
Il numero sarà sempre un numero intero positivo maggiore di 0. 
La tua funzione deve solo restituire il risultato, 
ciò che viene mostrato tra parentesi nell'esempio seguente è come raggiungi quel risultato e non ne fa parte, 
vedi i test di esempio.

Per esempio:
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(num: int) -> int:
    pass
"""

#Esercizio n°10
"""
Avendo un array di interi per la risoluzione di questo esercizio devi ritornare l'elemento più piccolo
Per esempio:
    find_smallest_int([34, 15, 88, 2]) -> 2
    find_smallest_int([34, -345, -1, 100]) -> -345
    
def find_smallest_int(arr: List[int]) -> int:
    pass
"""

