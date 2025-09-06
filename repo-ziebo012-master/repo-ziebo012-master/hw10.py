#scrabble_score==============================
# Purpose: calculates the score of a scrabble word
# Input Parameter(s): word-the word to calculate the score
# Return Value(s): Int-the score from the word
#==========================================
def scrabble_score(word):
    scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 
'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 
'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 
't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    if len(word)<=1:
        return scores[word]
    else:
        return scores[word[-1]]+scrabble_score(word[0:-1])

#relatively_prime==============================
# Purpose: finds greatest common divisor of x and y
# Input Parameter(s): x- the x value to find the common divisor
# y-the y value to find the common divisor
# Return Value(s): Bool-true or false if relatively prime or not
#==========================================
def relatively_prime(x,y):
    return gdc(x,y,2)


#gdc==============================
# Purpose: helper for finding greatest common divisor of x and y
# Input Parameter(s): x- the x value to find the common divisor
# y-the y value to find the common divisor
# d-divisor tracker
# Return Value(s): Bool-true or false if relatively prime or not
#==========================================
def gdc(x,y,d):
    if d==x or d==y:
        return True
    elif x%d==0 and y%d==0:
        return False
    else:
        return True and gdc(x,y,d+1)


#find_filepath==============================
# Purpose: finds a file path for the given file
# Input Parameter(s): 
# directory-list of directories to look for file in
# filename-name of file to be looking for
# Return Value(s): Bool-if no file found string-if file found giving its path
#==========================================
def find_filepath(directory,filename):
    if directory==[]:
        return False
    else:
        for i in directory:
            if type(i)==str:
                if i==filename:
                    return directory[0]+'/'+filename
            else:
                return find_filepath(i,filename)


