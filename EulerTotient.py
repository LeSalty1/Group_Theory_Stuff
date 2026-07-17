import math
from fractions import Fraction

# Avoiding sympy because it already has an Euler totient function. 
def is_prime(candidate): 
    for numb in range(2, int(candidate**0.5) + 1): 
        if candidate % numb == 0: 
            return False 
    return True

def euler_totient(n):
    if n == 1: 
        return 1
    if is_prime(n): 
        return n - 1 # The fact that phi(n) = n - 1 if n is prime should be clear. 
    primes = [] 
    for numb in range(2, n//2 + 1): 
        if is_prime(numb) and n % numb == 0: 
            primes.append(numb)
    for prime in primes: 
        n *= 1 - Fraction(1, prime)
    return n
