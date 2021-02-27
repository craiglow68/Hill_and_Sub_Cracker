#Author: Jacob Craiglow
#Description: Contains tools for tokenizing a string into unigrams,
#bigrams, and trigrams

#Builds and counts unigrams from cipherText.
#Returns a dictionary of unigrams and their counts.

def unigrams(cipherText):
    cipherUnigramFreq = {}

    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #unigram initialization
        cipherUnigramFreq[i] = 0

    for char in cipherText: #unigram counter
        cipherUnigramFreq[char] = cipherUnigramFreq[char] + 1

    return cipherUnigramFreq

#Builds and counts bigrams from cipherText.
#Returns a dictionary of bigrams and their counts.

def bigrams(cipherText):
    cipherLength = len(cipherText)
    cipherBigramFreq = {}

    for index in range(cipherLength-1): #bigram counter
        bigram = cipherText[index:index+2]

        if bigram in cipherBigramFreq:
            cipherBigramFreq[bigram] = cipherBigramFreq[bigram] + 1
        else:
            cipherBigramFreq[bigram] = 1
    
    return cipherBigramFreq

#Builds and counts trigrams from cipherText.
#Returns a dictionary of trigrams and their counts.

def trigrams(cipherText):
    cipherLength = len(cipherText)
    cipherTrigramFreq = {}

    for index in range(cipherLength-2): #Trigram counter
        trigram = cipherText[index:index+3]

        if trigram in cipherTrigramFreq:
            cipherTrigramFreq[trigram] = cipherTrigramFreq[trigram] + 1
        else:
            cipherTrigramFreq[trigram] = 1

    return cipherTrigramFreq
