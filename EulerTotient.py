import math
from fractions import Fraction
# STILL A WORK IN PROGRESS
# Avoiding sympy because it already has an Euler totient function. 
def is_prime(candidate): 
    for numb in range(2, int(candidate**0.5) + 1): 
        if candidate % numb == 0: 
            return False 
    return True

def euler_totient(n):
    result = Fraction(n, 1)
    if n == 1: 
        return 1
    primes = []
    for test in range(2, int(n**0.5) + 1): 
        if is_prime(test) and n % test == 0: 
            primes.append(test)
    for prime in primes: 
        result *= (1 - Fraction(1, prime))
    return int(result)
for i in range(2,51): 
    print(i, euler_totient(i))
