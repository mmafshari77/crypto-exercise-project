import random

def primesInRange(x, y):
    primeList = []
    for n in range(x, y):
        if isPrime(n):
            primeList.append(n)
            
    return primeList

def generateRandomPrime(x , y):
    primeList = primesInRange(x,y)
    randomPrime = random.choice(primeList)
    print('Generated random prime number: ', randomPrime)
    return randomPrime

def isPrime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

#Euclid's extended algorithm for finding the multiplicative inverse of two numbers    
def findMultiplicativeInverse(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise Exception('Modular inverse does not exist')
	return x % m    
