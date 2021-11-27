import number_theory_functions
from rsa_functions import RSA
from random import randrange


"""
M = 31415926
rsa = RSA.generate(10)
C = rsa.encrypt(M)
print("en", C)
MM = rsa.decrypt(C)
print(MM)

"""
print(number_theory_functions.modular_exponent(42,5425399,12215009))
print(5425399*3499, 3491*3499)