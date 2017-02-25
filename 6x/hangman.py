import string
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret = list(secretWord)
    for i in lettersGuessed:
        if i in secret:
            secret.remove(i)
    if len(secret) > 0:
        return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ' '
    used = {}
    for j in range(len(secretWord)):
        letter = secretWord[j]
        if letter in used:
            result += letter
        elif letter in lettersGuessed:
            used[letter] = True
            result += letter
            lettersGuessed.remove(letter)
        else:
            result += '_ '
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ' '
    alpha = list(string.ascii_lowercase)
    for i in lettersGuessed:
        alpha.remove(i)
    for j in alpha:
        result += j
    return result

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    
    while guesses > 0:
        print(lettersGuessed)
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            return
        availableLetters = getAvailableLetters(lettersGuessed)
        print('You have ' + str(guesses) + ' guesses left')
        print('Available letters: ' + availableLetters)
        userGuess = str(input('Please guess a letter: '))
        if userGuess in lettersGuessed: 
            print('Oops! You\'ve already used that letter: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            continue
        else:
            lettersGuessed.append(userGuess)
            if userGuess in secretWord:
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print('Oops! That letter is not in my word:' + str(getGuessedWord(secretWord, lettersGuessed)))
        guesses -= 1

    print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


hangman('tool')


