from typing import List 

"""
find_smallest_int([34, 15, 88, 2]) -> 2
find_smallest_int([34, -345, -1, 100]) -> -345
"""
arr = [34, -345, -1, 100]

def find_smallest_int(arr: List[int]) -> int:
    arr.sort()
    return arr[0]

print(find_smallest_int(arr))