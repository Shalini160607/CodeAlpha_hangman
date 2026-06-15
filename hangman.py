import random

words = ["python", "java", "computer", "science", "program"]

word = random.choice(words)

guessed = []
wrong = 0
max_wrong = 6

print("Welcome to Hangman Game")

while wrong < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed")
    elif guess in word:
        print("Correct!")
        guessed.append(guess)
    else:
        print("Wrong guess")
        guessed.append(guess)
        wrong += 1
        print("Attempts left:", max_wrong - wrong)

if wrong == max_wrong:
    print("You lost!")
    print("The word was:", word)