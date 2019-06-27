# import random

# # A list of words that 
# potential_words = ["quack", "words", "sandy", "total", "guess"]

# word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = "sandy"
word = list(word)

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = ['_'] 
maxfails = 6
fails = 0
guesses = guesses * len(word)
print(guesses)
guessed = []

while fails < maxfails:
    guess = input("Guess a letter: ")
    guessed.append(guess)
    if (guess in word):
        print("That is in the word!")
        index = word.index(guess)
        guesses[index] = guess
        if not ('_' in guesses):
            print(guesses)
            print("You got it!")
            quit()
    else:
        print("That is not in the word")
        fails += 1
    print(guesses)
    print("You have guessed: ")
    print(guessed)


	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
