#Author: Jacob Craiglow
#Description: Contains functionality to display a text with several 
#substitutions made.

#displayPartialSolution(cipherText, solutionSet)
#%cipherText - String literal
#%solutionSet - dictionary with character keys matching case of 
#cipherText and character values. e.x. {'O':'E', 'Z':'A'}

#Will print cipherText with characters substituted for values
#in the solutionSet. (O will be replaced with E for example above)
#Characters not present will be printed as '-'.

def displayPartialSolution(cipherText, solutionSet):
    solvedKeys = solutionSet.keys()

    for char in cipherText:
        if char in solvedKeys:
            print(solutionSet[char], end=" ")
        else:
            print('-', end=" ")
    
    print() #formating 