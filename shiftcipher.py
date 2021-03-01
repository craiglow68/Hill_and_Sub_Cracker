#Author: Jacob Craiglow
#Description: Contains tools for encoding and decoding a shift cipher. 

#encodeCipher(plainText, key)
#Returns a shift cipher encryption on plainText
#using the given key.
#Assumes mod 26 upper case alphabetic plain text

def encodeCipher(plainText, key):
    newText = ""
    plainText = plainText.upper()

    for char in plainText:
        newText = newText + chr((((ord(char) - 65) + key) % 26) + 65)

    return newText

#decodeCipher(cipherText, key)
#Returns a shift cipher decryption on cipherText
#using the given key.
#Assumes mod 26 upper case alphabetic cipher text

def decodeCipher(cipherText, key):
    newText = ""
    cipherText = cipherText.upper()

    for char in cipherText:
        newText = newText + chr((((ord(char) - 65) - key) % 26) + 65)

    return newText