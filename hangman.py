"""
CodeAlpha Task 1: Hangman Game
Text-based game: guess the word one letter at a time. Max 6 wrong guesses.
"""
import random

WORDS = ["python", "laptop", "internet", "keyboard", "program"]
MAX_WRONG = 6

STAGES = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def show_word(word, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN GAME ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("\nWord:", show_word(word, guessed))
        print("Guessed letters:", " ".join(sorted(guessed)) or "-")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        letter = input("Enter a letter: ").lower().strip()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.\n")
            continue
        if letter in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(letter)

        if letter in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

        if all(ch in guessed for ch in word):
            print("Word:", show_word(word, guessed))
            print(f"Congratulations! You won! The word was '{word}'.")
            return

    print(STAGES[MAX_WRONG])
    print(f"Game over! You lost. The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
