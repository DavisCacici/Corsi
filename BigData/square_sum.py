
from typing import List

# def square_sum(numbers: List[int]) -> int:
#     return sum(x ** 2 for x in numbers)
# print(square_sum([1, 2, 2]))
 

# def square_sum(numbers: List[int]) -> int:
#     result = 0
#     for i in numbers:
#         result += i ** 2
#     return result
# print(square_sum([1, 2, 2]))


def square_sum(numbers):
    i = 0
    result = 0
    while i < len(numbers):
        result += numbers[i] ** 2
        i+=1
    return result
print(square_sum([1, 2, 2]))