#Author: Jacob Craiglow
#Description: Contains tools, charts, and a UI to help break a shift cipher
#Usage: python shiftTools.py cipherText

from displayPartial import displayPartialSolution
from shiftcipher import decodeCipher, encodeCipher
from tokenizer  import *
import sys

if len(sys.argv) != 2:
    print("Incorrect usage.")
    print('Usage: python shiftTools.py cipherText')
    sys.exit()

cipherText = str(sys.argv[1])

cipherUnigramFreq = unigrams(cipherText)
cipherBigramFreq = bigrams(cipherText)
cipherTrigramFreq =trigrams(cipherText)

sortedUnigrams = sorted(cipherUnigramFreq.items(), key=lambda x: x[1], reverse=True)
sortedBigrams = sorted(cipherBigramFreq.items(), key=lambda x: x[1], reverse=True)
sortedTrigrams = sorted(cipherTrigramFreq.items(), key=lambda x: x[1], reverse=True)

#Capital I not included
unigramFreq = {'A':8.167, 'B':1.492, 'C':2.782, 'D':4.253, 'E':12.702, 'F': 2.228, 
    'G':2.015, 'H':6.094, 'I': 6.966, 'J':0.153, 'K':0.772, 'L':4.025, 'M':2.406, 
    'N':6.749, 'O':7.507, 'P':1.929, 'Q':0.095, 'R':5.987, 'S':6.327, 'T':9.056, 
    'U':2.758, 'V':0.978, 'W':2.360, 'X':0.150, 'Y':1.974, 'Z':0.074}
sortedUnigramFreq = sorted(unigramFreq.items(), key=lambda x: x[1], reverse=True)

bigramFreq = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ON', 'ES', 'ST', 'EN', 'AT', 'TO', 'NT', 'HA'] #In sorted order
trigramFreq = ['THE', 'ING', 'AND', 'HER', 'ERE', 'ENT', 'THA', 'NTH', 'WAS', 'ETH', 'FOR', 'DTH', 'HAT', 'SHE', 'ION'] #In sorted order

print("Top 10 Unigrams in Engligh Language:")
for x in range(10):
    print(sortedUnigramFreq[x])
print("========================================================")

print("Top 15 Bigrams in Engligh Language:")
for x in range(7):
    print(bigramFreq[x] + "\t" + bigramFreq[7 + x])
print("   \t" + bigramFreq[14])
print("========================================================")

print("Top 15 Trigrams in Engligh Language:")
for x in range(7):
    print(trigramFreq[x] + "\t" + trigramFreq[7 + x])
print("   \t" + trigramFreq[14])
print("========================================================")

print("Top 15 Unigram frequencies in cipher:")
print(sortedUnigrams[:15])
print("=========================================================")
print("Bigram frequencies occuring more than once:")
print([x for x in sortedBigrams if x[1]>1])
print("=========================================================")
print("Trigram frequencies occuring more than once:")
print([x for x in sortedTrigrams if x[1]>1])
print("=========================================================")

cont = True
solutionSet = {}

while(cont):
    print('''To build solution set type substitutions of the form:
    x-y press enter
    a-b press enter
    q to quit
    s to show partial solution
    c to clear solution set
    or k to try a key''')
    
    flag = True

    while(flag):
        temp = input()
        temp = temp.upper()

        if temp == 'Q':
            flag = False
            cont = False
        elif temp == 'S':
            print("Partial Solution:")
            displayPartialSolution(cipherText, solutionSet)
            print("=========================================================")
        elif temp == 'C':
            solutionSet = {}
        elif temp == 'K':
            print("Enter Key:")
            k = input()
            print(decodeCipher(cipherText, int(k)))
        elif(len(temp)!=3):
            print("incorrect format")
        else:    
            original = temp[0]
            new = temp[2]
            solutionSet[original] = new