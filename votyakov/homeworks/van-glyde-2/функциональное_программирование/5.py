# def reduce_sum(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] + reduce_sum(numbers[1:])

from functools import reduce

def reduce_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)