def is_prime(n):
    if n == 1:
        return False
    return len(list(filter(lambda x: n%x == 0, range(2, int(n**(0.5)) + 1)))) == 0