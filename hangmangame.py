import random


words = ['kangaroo', 'platypus', 'koala', 'wombat', 'echidna', 'dingo', 'tasmanian devil', 'wallaby']


word = random.choice(words)
guessed = "_" * len(word)
word = word.lower()
guessed = list(guessed)
lstGuessed = []
letter = input("Guess letter: ")
tries = 6


hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while tries > 0:
    print(hangman[(len(hangman) - 1) - tries])
    print(f"Word: {' '.join(guessed)}")
    print(f"Tries left: {tries}")
    print(f"Guessed letters: {', '.join(lstGuessed)}")
    if letter.lower() in lstGuessed:
        print("You already guessed that letter.")
    elif letter.lower() in word:
        print("Good job! That letter is in the word!")
        for i in range(len(word)):
            if word[i] == letter.lower():
                guessed[i] = letter.lower()
        lstGuessed.append(letter.lower())
    else:
        print("Sorry, that letter is not in the word. Try again.")
        tries -= 1
        lstGuessed.append(letter.lower())

    if "_" not in guessed:
        print("Congratulations! You've guessed the word!")
        break
    letter = input("Guess letter: ")

else:
    print(hangman[-1])
    print("Sorry, you've been hanged!")
    print(f"The word was: {word}")

