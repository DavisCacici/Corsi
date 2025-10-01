from typing import List

def count_sheeps(array_of_sheep: List[bool]) -> int:
    return array_of_sheep.count(True)

def count_sheeps_nuovo(array_of_sheep: List[bool]) -> int:
    s = 0
    for i in array_of_sheep:
        if i == True :
            s += 1
    return s