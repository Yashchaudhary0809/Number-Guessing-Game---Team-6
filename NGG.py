# Developer 1: Core Game Logic
import random
import time

class GameEngine:
    def __init__(self, initial_level=1):
        self.level = initial_level
        self.max_attempts = 10

    def generate_challenge(self):
        """Generate game challenge based on current level."""
        upper_bound = 100 * self.level
        return random.randint(1, upper_bound), 1, upper_bound


# Developer 2: User Interface and Interaction
class GameUI:
    @staticmethod
    def display_instructions():
        """Display game instructions before starting."""
        print("\n🎮 NUMBER GUESSING GAME INSTRUCTIONS 🎮")
        print("1. You'll guess a random number in an increasing difficulty range")
        print("2. Each level increases the number range and reduces attempts")
        print("3. Hints will guide you closer to the target number")
        print("4. Aim to guess with fewer attempts for a better score!")
        print("5. Enter 'q' anytime to quit the game\n")
        input("Press Enter to start the game...")

    @staticmethod
    def get_user_guess(lower, upper):
        """Prompt user for guess with input validation."""
        while True:
            try:
                guess = input(f"Guess a number between {lower} and {upper}: ")
                if guess.lower() == 'q':
                    return None
                return int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")


# Developer 3: Game Mechanics and Logic
class NumberGuessingGame:
    def __init__(self):
        self.engine = GameEngine()
        self.ui = GameUI()

    def play(self):
        """Main game loop with level progression."""
        self.ui.display_instructions()

        while True:
            target, lower, upper = self.engine.generate_challenge()
            attempts = 0
            level_won = False  # Track whether the user has won the current level

            print(f"\n--- Level {self.engine.level} ---")
            print(f"Guess the number between {lower} and {upper}")

            while attempts < self.engine.max_attempts:
                guess = self.ui.get_user_guess(lower, upper)

                if guess is None:
                    print("Game ended. Thanks for playing!")
                    return

                attempts += 1

                if guess == target:
                    print(f"🎉 Correct! You won Level {self.engine.level}")
                    level_won = True  # Mark the level as successfully completed
                    break

                hint = "Higher" if guess < target else "Lower"
                print(f"Try {hint}. Attempts left: {self.engine.max_attempts - attempts}")

            if not level_won:  # If the user didn't win, show the game over message
                print(f"Game Over! The number was {target}")
                break  # End the game if the user loses

            # Ask to continue to the next level if the user won
            if level_won and input("Continue to next level? (y/n): ").lower() != 'y':
                break

            self.engine.level += 1
            self.engine.max_attempts = max(10 - self.engine.level + 1, 3)


def main():
    game = NumberGuessingGame()
    game.play()


if __name__ == "__main__":
    main()
