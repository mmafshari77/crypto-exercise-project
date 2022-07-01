import random
from maths_utils import isPrime, findMultiplicativeInverse
from math import gcd

def generateKeypair(p, q):
    if not (isPrime(p) and isPrime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = (p-1) * (q-1)

    b = random.randrange(1, phi)
    g = gcd(b, phi)
  
    while g != 1:
        b = random.randrange(1, phi)
        g = gcd(b, phi)

    a = findMultiplicativeInverse(b, phi)

    # Public key is (b, n) and private secret is (a, n)
    return ((b, n), (a, n))

def encrypt(publicKey, plaintext):
    key, n = publicKey            
    numberRepr = [ord(char) for char in plaintext]
    print("Number representation before encryption: ", numberRepr)
    cipher = [pow(ord(char),key,n) for char in plaintext]
    return cipher

def decrypt(privateSecret, ciphertext):
    key, n = privateSecret
    numberRepr = [pow(char, key, n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    print("Decrypted number representation is: ", numberRepr)
    return ''.join(plain)