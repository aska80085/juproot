def sum_even_numbers(numbers):
    s = 0
    for i in numbers:
        if i%2 == 0:
            s += i
    return s