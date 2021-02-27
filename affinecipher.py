#Author: Jacob Craiglow
#Description: Contains tools for encoding and decoding an affine cipher. 

import math

#checkKeyValidity(key, mod)
#key is a tuple (a,b)
#checks if (a,b) is a valid key for
#an affine cipher in the chosen mod

def checkKeyValidity(key, mod):
    if (math.gcd(key[0], mod) > 1):
        return False
    else:
        return True

#multiplicativeInverse(key, mod)
#key is an integer
#returns the multiplicative inverse 
#of key in the form keyInverse * key = 1 mod mod
#returns None if it does not exist

def multiplicativeInverse(key, mod):
    x = 0
    y = 1
    u = 1
    v = 0
    a = key
    b = mod

    while a != 0: 
        quotient = b//a
        remainder = b%a 
        m = x-u*quotient
        n = y-v*quotient
        b = a 
        a = remainder
        x = u
        y = v
        u = m
        v = n
        
    gcd = b 

    if gcd != 1:
        return None
    else:
        return x % mod 
    
#encodeCipher(plainText, key)
#Key is a tuple of integers of the form: (a, b)
#Returns an affine cipher encryption on plainText
#using the given key.
#Assumes mod 26 upper case alphabetic plain text

def encodeCipher(plainText, key):
    cipherText = ""

    for char in plainText:
        cipherText = cipherText + chr(((((ord(char) - 65) * key[0]) + key[1]) % 26) + 65) 

    return cipherText

#decodeCipher(cipherText, key)
#Key is a tuple of integers of the form: (a, b)
#Returns an affine cipher decryption on cipherText
#using the given key.
#Assumes mod 26 upper case alphabetic cipher text

def decodeCipher(cipherText, key):
    plainText = ""

    multInverse = multiplicativeInverse(key[0], 26)

    if multInverse == None: 
        return "Invalid Key for mod 26 cipher"

    for char in cipherText:
        plainText = plainText + chr(((multInverse * ((ord(char) - 65) - key[1])) % 26) + 65)
    
    return plainText

#breakKey(c1, p1, c2, p2)
#Returns the affine cipher key used to encrypt 
#p1 to c1 and p2 to c2.
#Returns None if no multiplicative inverse is found

def breakKey(c1, p1, c2, p2):
    p = ord(p1) - 65
    q = ord(p2) - 65
    r = ord(c1) - 65
    s = ord(c2) - 65

    d = (p - q) % 26
    dInverse = multiplicativeInverse(d, 26)
    if dInverse == None:
        return None

    a = (dInverse * (r - s)) % 26
    b = (dInverse * (p * s - q * r)) % 26

    return (a, b)