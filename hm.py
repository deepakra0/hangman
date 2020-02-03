import requests

Key = requests.get('https://random-word-api.herokuapp.com/key?').text
GetWordURL = 'https://random-word-api.herokuapp.com/word?key=' + Key + '&number=1'
PlayAgain = 'Y' 

while(PlayAgain != 'N'):
    print('Fetching new word..', end = '')
    Word = (requests.get(GetWordURL).text[2:-2]).upper()
    print('Done')
    CorrectGuesses = 6
    CharGussedCorrectly = len(Word)
    GuessedWord = '-' * len(Word)
    while(CorrectGuesses > 0 and CharGussedCorrectly > 0):
        print (GuessedWord)
        GuessedChar = input('Your choice please: ')[0].upper()
        if(Word.find(GuessedChar) == -1):
            CorrectGuesses -= 1
        else:
            for m in range(len(Word)):
                if(Word[m] == GuessedChar):
                    GuessedWord = GuessedWord[:m] + GuessedChar + GuessedWord[(m + 1):]
                    CharGussedCorrectly -= 1
        print('You have ', CorrectGuesses, ' more tries left')
    if( CorrectGuesses > 0):
        print('Correctly gussed the word ', Word,'. ', end='')
        PlayAgain = input('Do you wish to continue: ')[0].upper()
    else:
        print('Unable to guess the word. the word was', Word, '. ', end='')
        PlayAgain = input('Do you wish to continue: ')[0].upper()
print('Game ends..')

