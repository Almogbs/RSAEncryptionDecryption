import number_theory_functions 
from random import randrange

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod

    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        found_p_and_q = False          
        while found_p_and_q == False:
            p = number_theory_functions.generate_prime(digits//2+(digits%2))
            q = number_theory_functions.generate_prime(digits//2+(digits%2))
            if (p*q >= 10**(digits-1) and p*q < 10**(digits)):
                found_p_and_q = True
        N=p*q
        k=(p-1)*(q-1)
        found_e=False
        while found_e==False:
            n = randrange(1, k)
            if (number_theory_functions.extended_gcd(k,n)[0]==1):
                e=n
                found_e=True
        d=number_theory_functions.modular_inverse(e, k)
        return RSA((N,e),(N,d))

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        e = self.public_key[1]
        N = self.public_key[0]
        c = number_theory_functions.modular_exponent(m, e, N)

        return c

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        N = self.private_key[0]
        d = self.private_key[1]
        m = number_theory_functions.modular_exponent(c, d, N)

        return m    