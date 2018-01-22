

import random
import string

WORDLIST_FILENAME = "C:\Users\SHRIKUMAR\Desktop\python\hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    c=0
    k=0
    for char in secretWord:
        if secretWord[k] in lettersGuessed:
            c=c+1
        k=k+1
    if c == len(secretWord):
        z=True
    else: z = False
    return z



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i=[]
    s=''
    k=0
    l=len(secretWord)
    for char in secretWord:
        if secretWord[k] in lettersGuessed:
            i.append(secretWord[k])
        else: i.append('_')
        k=k+1
    for n in i:
        s=s+n
    
    return s



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    l=''
    s=string.ascii_lowercase
    st=[]
    i=0
    for char in s:
        k=s[i]
        st.append(k)
        i=i+1
    for h in range(len(lettersGuessed)):
        if lettersGuessed[h] in st:
            j=lettersGuessed[h]
            st.remove(j)
    for n in st:
        l=l+n
    return l
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    
    '''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word which is '+ str(len(secretWord))+ ' letters long'
    print '-----------'
    numguess=8
    lettersGuessed=[]
    while (getGuessedWord(secretWord,lettersGuessed)==secretWord or numguess>0):
       print 'You have '+ str(numguess) + ' guesses left'
       availableletters=getAvailableLetters(lettersGuessed)
       print 'Available Letters: ' + str(availableletters)
       xlh = str(raw_input('Please guess a letter: '))
       x = xlh.lower()
       if x in lettersGuessed:
          print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed)
          print '-----------'
       else:
          lettersGuessed.append(x)
          if x in secretWord:
             print 'Good guess:' + getGuessedWord(secretWord,lettersGuessed)
             print '-----------'
             if getGuessedWord(secretWord,lettersGuessed)==secretWord:break
          
          else:
             numguess=numguess-1
             print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord,lettersGuessed)
             print '-----------'
          
    y=getGuessedWord(secretWord,lettersGuessed)
    if y==secretWord:
       print 'Congratulations, You won!'
    else:
       print 'Sorry, you ran out of guesses. The word was ' + str(secretWord)




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
