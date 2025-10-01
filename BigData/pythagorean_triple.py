from typing import List
"""
    integers = [3, 4, 5]
    integers = [5, 3, 4]
"""

def pythagorean_triple(integers: List[int]) -> bool:
    integers.sort()
    if integers[0]**2 + integers[1]**2 == integers[2]**2:
        return True
    return False