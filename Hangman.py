import random

word_list = ["python", "hangman", "developer", "programming", "variable",
    "function", "keyboard", "monitor", "computer", "internet",
    "algorithm", "database", "software", "hardware", "debug",
    "compile", "execute", "syntax", "object", "class"]

select_word = random.choice(word_list)
print("Welcome to Hangman!")

for _ in range(len(select_word)):
    print("_", end=" ")
print("\n")

lives = 6
display_word = ["_"] * len(select_word)
guessed_letters = []
wrong_guesses = []

while "_" in display_word and lives > 0:
    guess = input("Type your guess!: ").lower()
    if guess in guessed_letters:
        print("You already guessed this word")
    elif guess in select_word:
        for index, letter in enumerate(select_word):
            if letter == guess:
                display_word[index] = guess
        print("You're Correct!")
    else:
        lives -= 1
        print("Wrong!")

    guessed_letters.append(guess)
    print("Current word: "," ".join(display_word))
    print(f"Lives: {lives}")

