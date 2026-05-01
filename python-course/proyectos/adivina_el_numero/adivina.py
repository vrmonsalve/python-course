# ============================================================
# Project 02 — Guess the Number
# ============================================================
# The computer picks a random number between 1 and 100.
# The player has to guess it. The program gives hints.

import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("=" * 35)
    print("   🎯 Guess the Number Game!")
    print("=" * 35)
    print(f"I am thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} → Your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                attempts -= 1
                continue

            if guess == secret:
                print(f"\n🎉 Correct! The number was {secret}.")
                print(f"You got it in {attempts} attempt(s)!")
                return True
            elif guess < secret:
                remaining = max_attempts - attempts
                print(f"Too low! ⬆️  ({remaining} attempts left)\n")
            else:
                remaining = max_attempts - attempts
                print(f"Too high! ⬇️  ({remaining} attempts left)\n")

        except ValueError:
            print("Please enter a valid number.\n")

    print(f"\n😢 Game over! The number was {secret}.")
    return False

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! 👋")
            break
        print()

if __name__ == "__main__":
    main()
