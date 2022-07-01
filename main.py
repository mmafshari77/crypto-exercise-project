from operator import mod
from statistics import mode
import sys
from unittest import case
from maths_utils import *
from maths_utils import generateRandomPrime
from rsa import *

def fromScratch():
    primeNumberLowerbound = int(input("Enter your prefered lowerbound for generating prime: "))
    primeNumberUpperbound = int(input("Enter your prefered upperbound for generating prime: "))
    p = generateRandomPrime(primeNumberLowerbound, primeNumberUpperbound)
    q = generateRandomPrime(primeNumberLowerbound, primeNumberUpperbound)
    while (p == q):
        p = generateRandomPrime(primeNumberLowerbound, primeNumberUpperbound)
        q = generateRandomPrime(primeNumberLowerbound, primeNumberUpperbound)     
    pub, priv = generateKeypair(p, q)
    while True:
        print("Let's seee what you want to do:")
        print("\t1. Encrypt using my public key (RSA)")
        print("\t2. Decrypt using my private key (RSA)")
        print("\t3. Encrypt using others public key (RSA)")
        userInput = int(input("[1 or 2 or 3]: "))
        match userInput:
            case 1:
                print(encrypt(pub, input("Enter your message: ")))
                
            case 2: 
                arr = []
                a = int(input("Enter elements of the ciphertext (-1 to stop): "))
                while a != -1:
                    arr.append(a)
                    a = int(input("Enter elements of the ciphertext (-1 to stop): "))
                print(decrypt(priv,arr))
            case 3:
                return

if __name__=="__main__":
    if(sys.argvs[1] == "-f"):
        print("Searching current dirctory for 'my.priv', 'my.pub' and 'other.pub' files...")
        myPriv = open(file="my.priv", modee="r")
        myPub = open(file="my.pub", mode="r")
        otherPub = open(file="other.pub", mode="r")
    else:
        fromScratch()

