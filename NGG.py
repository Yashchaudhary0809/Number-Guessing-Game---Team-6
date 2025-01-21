#NUMBER GUESSING GAME 
import random

# Creating a Function
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Set the range for the random number
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        
        # Generate a random number between the specified bounds
        number_to_guess = random.randint(lower_bound, upper_bound)
        attempts = 0
        guessed = False
        
        print(f"\nI have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")
        
        # Entering into the loop
        while not guessed:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("You are Too low! Try again.")
            elif user_guess > number_to_guess:
                print("You are Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True
        
        # Asking if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Creating function for main menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Start Number Guessing Game")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main_menu()