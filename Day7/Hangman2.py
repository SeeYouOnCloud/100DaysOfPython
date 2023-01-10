import random

# The list of words to choose from
words = ["python", "java", "javascript", "computer", "science"]

# Choose a random word from the list
word = random.choice(words)

# Create a list of underscores the same length as the word
display = ["_"] * len(word)

# The number of wrong guesses the user has made
wrong_guesses = 0

# The list of letters that the user has already guessed
guessed_letters = []

# The maximum number of wrong guesses allowed before the game is lost
max_wrong_guesses = 6

while "_" in display and wrong_guesses < max_wrong_guesses:
    # Print the current state of the word to guess
    print(" ".join(display))
    print("Guessed letters: ", " ".join(guessed_letters))

    # Ask the user for a letter
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    # Add the letter to the list of guessed letters
    guessed_letters.append(guess)

    if guess in word:
        # Replace underscores with the correctly guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Incorrect. You have", max_wrong_guesses - wrong_guesses, "guesses left.")

# Check if the user won or lost
if "_" not in display:
    print("Congratulations! You won! The word was", word)
else:
    print("Sorry, you lost. The word was", word)
