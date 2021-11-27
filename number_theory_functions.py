from random import randrange
from math import pow

def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if(a==0):
        return (b, b, 1) 
    if(b==0):
        return (a, 1, a) 
    (d, x1, y1) = extended_gcd(b,a%b)
    return (d, y1, x1-y1*(a//b))






def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns     
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    (d,x) = (extended_gcd(a,n)[0], extended_gcd(a,n)[1])
    if d!=1:
        return None
    return x%n    

def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    result: such that result == (a**d) % n
    """ 
    reversed_bin_d = bin(d)[2:][::-1]
    result = 1
    len_bin_d = len(reversed_bin_d)

    for i in range(len_bin_d):
        result = (result*a**int(reversed_bin_d[i]))%n
        a = (a**2)%n
    
    return result

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for _ in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None