import sys
#import numpy as np # used for the un used levenshtein fucntion
from fuzzywuzzy import process
import GrabAudio as GA
#============================================================================================================================
# Useful function for string comparason, if ratio_calc=True outputs a normalised ratio of how similar the two strings are
# This is useful for small strings that you know are v similar but falls short for wildly abstract string processing
# (which we are using here). so instead i use FuzzyWuzzy library (lol what a name)
def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
        taken from: https://www.datacamp.com/community/tutorials/fuzzy-string-python
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])
#============================================================================================================================

def readGen():
    for line in open("outpQuotParsed.txt", encoding="ANSI"):
        yield line

# Below we use the FuzzyWuzzy library
# First we need to sanitise

print("""
This python script takes a string as an input,
and trys to select the best glados quote from
the txt file 'GladosQuotes.txt'

Type your sentance:
""")

# cheap memory inefficient way:
strcomList = []
for item in readGen():
    strcomList.append(GA.sanitizeString(item))

def GetMostSimilarString(comp, listComp):
    # sanitize input string
    comp = GA.sanitizeString(comp)
    # This is where the fun begins
    Ratios = process.extract(comp,listComp)
    highest = process.extractOne(comp,listComp)
    return highest

while True:
    statment = input(">>")
    print(GetMostSimilarString(statment, strcomList))
    GA.FinalPlaySound(GetMostSimilarString(statment, strcomList)[0])