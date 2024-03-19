# hangmangame

import random: This line imports the random module, which provides various functions for generating random numbers and selecting random elements from lists.

words = ['kangaroo', 'platypus', 'koala', 'wombat', 'echidna', 'dingo', 'tasmanian devil', 'wallaby']: This line creates a list called words containing various animal names.

word = random.choice(words): This line selects a random word from the words list and assigns it to the variable word.

guessed = "_" * len(word): This line creates a string of underscores (_) with the same length as the selected word and assigns it to the variable guessed. This string represents the letters of the word that the player needs to guess.

word = word.lower(): This line converts the randomly selected word to lowercase. This ensures that letter comparisons later in the code are case-insensitive.

guessed = list(guessed): This line converts the string of underscores to a list of characters. This conversion allows individual characters to be replaced as the player makes correct guesses.

lstGuessed = []: This line initializes an empty list called lstGuessed, which will store the letters guessed by the player.

letter = input("Guess letter: "): This line prompts the player to input a letter guess and assigns the input to the variable letter.

tries = 6: This line initializes the variable tries to 6, representing the number of attempts the player has to guess the word.

The hangman variable contains ASCII art representations of the hangman at different stages of the game.

The while loop is the main game loop. It runs as long as the player has remaining attempts (tries > 0).

Inside the loop:

It prints the current state of the hangman (print(hangman[(len(hangman) - 1) - tries])).
It prints the current state of the word being guessed (print(f"Word: {' '.join(guessed)}")).
It prints the number of tries left (print(f"Tries left: {tries}")).
It prints the letters already guessed by the player (print(f"Guessed letters: {', '.join(lstGuessed)}")).
It checks if the guessed letter is already in the list of guessed letters, if it is, it prints a message indicating that the letter was already guessed.
If the guessed letter is in the word, it updates the guessed word and appends the guessed letter to the list of guessed letters.
If the guessed letter is not in the word, it decrements the number of tries remaining and appends the guessed letter to the list of guessed letters.
After the loop, it checks if the player has successfully guessed the word (if "_" not in guessed:). If so, it prints a congratulatory message and breaks out of the loop.

If the player runs out of tries, it prints the final state of the hangman, a message indicating that the player has lost, and reveals the correct word.
