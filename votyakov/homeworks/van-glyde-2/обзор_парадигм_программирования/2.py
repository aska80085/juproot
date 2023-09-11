def sum_even_numbers(numbers):
    s = 0
    if len(numbers) != 0:
        if numbers[0] % 2 == 0:
            return numbers[0] + sum_even_numbers(numbers[1:])
        else:
            return sum_even_numbers(numbers[1:])
    else:
        return 0