# RSAEncryptionDecryption

## Methods:

### - generate:
   - Purpose:    Create RSA encryption object
   - Parameters: digits - lengh of the prime number used in the decrypt (higher is more secure)
   - Return:     RSA encryption object
### - encrypt:
   - Purpose:    Encrypt message
   - Parameters: M - message to encrypt
   - Return:     c - encrypted message
### - decrypt:
   - Purpose:    Decrypt the message
   - Parameters: c - message to decrypt
   - Return:     m - decrypted message
   
#### usage:
        M = "you cant handle the truth"
        rsa = RSA.generate(15)
        C = rsa.encrypt(M)
        MM = rsa.decrypt(C)
        
        

