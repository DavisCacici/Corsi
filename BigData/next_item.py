from typing import Any


# def next_item(array: Any, item: Any) -> Any:
#     if(item not in array):
#         return None
    
#     indice = array.index(item)
#     if(indice == len(array)-1):
#         return None
    
#     return array[indice+1]

def next_item2(array: Any, item: Any) -> Any:
    for i in range(0, len(array)-1):
        if item == array[i]:
            return array[i+1]
    
    return None


print(next_item2(['Joe', 'Bob', 'Sally'], 'Joe'))
        


# print(next_item(['Joe', 'Bob', 'Sally'], 'Joe'))