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
"""
def new_join(separate: str, arr: List[str]) -> str:
    pass


