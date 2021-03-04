from hillcipher import decryptHill, decryptionKey, matrixMult
from tokenizer import bigrams
import sys

test = [[8, 7], [5, 17]]

if len(sys.argv) != 2:
    print("Incorrect usage.")
    print('Usage: python hillTools.py cipherText.txt')
    sys.exit()

f = open(str(sys.argv[1]))
cipherText = f.read()
f.close()

cipherText = cipherText.strip()

cipherBigramFreq = bigrams(cipherText)

sortedBigrams = sorted(cipherBigramFreq.items(),
                       key=lambda x: x[1], reverse=True)

bigramFreq = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ON',
              'ES', 'ST', 'EN', 'AT', 'TO', 'NT', 'HA']  # In sorted order

print("Top 15 Bigrams in Engligh Language:")
for x in range(7):
    print(bigramFreq[x] + "\t" + bigramFreq[7 + x])
print("   \t" + bigramFreq[14])
print("========================================================")

print("Bigram frequencies occuring more than once:")
print([x for x in sortedBigrams if x[1] > 1])
print("=========================================================")

cont = True

while(cont):
    print('''
    p to show stats
    t to try a combination
    or q to quit''')

    flag = True

    while(flag):
        temp = input()
        temp = temp.upper()

        if temp == 'Q':
            flag = False
            cont = False
        elif temp == 'P':
            print("Top 15 Bigrams in Engligh Language:")
            for x in range(7):
                print(bigramFreq[x] + "\t" + bigramFreq[7 + x])
            print("   \t" + bigramFreq[14])
            print("========================================================")

            print("Bigram frequencies occuring more than once:")
            print([x for x in sortedBigrams if x[1] > 1])
            print("=========================================================")
        elif temp == 'T':
            print("Enter first pair to try in the form: p1 p2 c1 c2")
            firstInput = input().upper().split()
            pMatrix = [[ord(firstInput[0])-65, ord(firstInput[1])-65]]
            cMatrix = [[ord(firstInput[2])-65, ord(firstInput[3])-65]]

            print("Enter second pair to try in the form: p3 p4 c3 c4")
            secondInput = input().upper().split()
            pMatrix.append([ord(secondInput[0])-65, ord(secondInput[1])-65])
            cMatrix.append([ord(secondInput[2])-65, ord(secondInput[3])-65])

            xInverse = decryptionKey(pMatrix)

            if xInverse != None:
                keyAttempt = matrixMult(cMatrix, xInverse)
                keyAttemptInverse = decryptionKey(keyAttempt)

                if keyAttemptInverse != None:
                    print("Key:")
                    print(keyAttempt)
                    print("Decryption:")
                    print(decryptHill(cipherText, keyAttempt, 2))
                else:
                    print("Key has no inverse, Incorrect Key:")
                    print(keyAttempt)
            else:
                print("plain text matrix has no inverse")
        elif(len(temp) != 1):
            print("incorrect format")
        else:
            temp = ""
