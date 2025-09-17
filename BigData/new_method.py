from typing import List


def values(a:bool):
    # a = True
    if a:
        return True
    else:
        return False
    
# print(values(False))

def new_replace(analisi: str, da_sostituire: str, nuovo_carattere: str):
    result = ''
    for i in range(0,len(analisi)):
        if(analisi[i]==da_sostituire):
            result+=nuovo_carattere
        else:
            result+=analisi[i]
    return result


"""
Replicare la funzione join
- Navighiamo la lista di stringhe
- Prendere l'elemento e inserirlo dentro una varibile (di ritorno)
- Aggiungere il carattere di separazione
- Fare attenzione di non inserire il carattere di separazione all'ultimo elemento dell'array
"""
def new_join(separate: str, arr: List[str]) -> str:
    result = ''
    # for i in range(0, len(arr)):
    #     if i == len(arr)-1:
    #         result += arr[i]
    #     else:
    #         result += arr[i] + separate
    for i in range(0, len(arr)-1):
        result += arr[i] + separate
    return result + arr[-1]

print(new_join(' ', ['Hello', 'World', '?']))


# arr = ["-", "?", "%", "/", "=", '^']
# print(arr[-1])
