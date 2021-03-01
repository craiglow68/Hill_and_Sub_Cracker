import math

#   decryptHill(ciphertext, key, m)
# Returns decrypted ciphertext that has been encrypted using
# a hill cipher with key and m=m.
#
# ciphertext = Code to be decrypted. Must be uppercase
# key = mxm matrix used to encode ciphertext
# m = Dimensions of key matrix as well as number of characters encoded


def decryptHill(ciphertext, key, m):
    plaintext = ""
    cipherLen = len(ciphertext)
    keyInverse = decryptionKey(key)

    for i in range(0, cipherLen, 2):  # Start at 0, Stop at Length of cipher, Step by 2
        if i == cipherLen-(m-1):
            break

        tempCode = [[]]
        for j in range(m):
            tempCode[0].append(ord(ciphertext[i + j])-65)

        ptVector = matrixMult(tempCode, keyInverse)

        for l in ptVector[0]:
            plaintext = plaintext + chr(l + 65)

    return plaintext


#   matrixMult(x, y)
# Returns matrix * matrix y.
# Does no error checking.

def matrixMult(x, y):
    ret = []

    # iterate through rows of X
    for i in range(len(x)):
        ret.append([])
        # iterate through columns of Y
        for j in range(len(y[0])):
            ret[i].append([])
            sum = 0
            # iterate through rows of Y
            for k in range(len(y)):
                sum = sum + (x[i][k] * y[k][j])

            ret[i][j] = sum % 26

    return ret

#   decryptionKey(key)
# Returns the decryption key of a 2x2 matrix key in mod 26.
#
# key = 2D array
# Key represents an 2x2 matrix
# example key = [[2, 4], [4, 3]]
# this represents a 2x2 matrix of the form [2 4]
#                                          [4 3]
# Returns a 2D array if key exists. If it does not, returns None


def decryptionKey(key):
    determinant = getDeterminant(key)

    if (determinant == None):
        return None
    else:
        invert = [[key[1][1] % 26, (key[0][1]*-1) %
                   26], [(key[1][0]*-1) % 26, key[0][0] % 26]]

    ret = [[], []]

    for i in range(2):
        ret[i].append((invert[i][0] * determinant) % 26)
        ret[i].append((invert[i][1] * determinant) % 26)

    return ret

#   multiplicativeInverse(key, mod)
# key is an integer
# returns the multiplicative inverse
# of key in the form keyInverse * key = 1 mod mod
# returns None if it does not exist


def multiplicativeInverse(key, mod):
    x = 0
    y = 1
    u = 1
    v = 0
    a = key
    b = mod

    while a != 0:
        quotient = b//a
        remainder = b % a
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

#   GetDeterminant(key)
# Returns the mod 26 determinant of 2x2 key if it exists.
# Returns None if it does not.
#
# key = 2D array
# Key represents an 2 x 2 matrix
# example key = [[2, 4], [4, 3]]
# this represents a 2x2 matrix of the form [2 4]
#                                          [4 3]


def getDeterminant(key):
    a = key[0][0] * key[1][1]
    b = key[0][1] * key[1][0]

    determinant = a - b

    determinant = determinant % 26

    if determinant == 0:  # Effectively short-circuits multiplicativeInverse
        return None

    ret = multiplicativeInverse(determinant, 26)

    if ret == None:
        return None

    return ret
