from math import sqrt

"""
Check if a number is prime.
"""
def is_prime(n: int) -> bool:
    # we only need to check numbers from 2 .. sqrt(n)
    # since (sqrt(n) + 1)^2 = n + 1 + 2*sqrt(n) > n
    max_possible_divisor = int(sqrt(n))
    for i in range(2, max_possible_divisor + 1):
        if n % i == 0:
            return False
    return True

def test():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(2**16 + 1) == True

test()
