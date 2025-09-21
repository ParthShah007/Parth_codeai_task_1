import random
import sys

# loading the file and returning only the secret word
def get_secret_word(file_name):
    # Error handling skills!
    try:
        with open(file_name, "r") as file:
            words = [word.strip().lower() for word in file if word.strip()]
        if not words:
            print("Error: The word list is empty.")
            sys.exit(1)
        secret = random.choice(words)
        return secret
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        sys.exit(1)

# compare guess with secret word
def check_guess(secret_word, guess):
    feedback = ['absent'] * 5
    secret_temp = list(secret_word)  # list helps us work on indexing and manipulation

    # 1st: check for correct letters
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback[i] = 'correct'
            secret_temp[i] = None  # Mark as read basically for correct

    # 2nd: check for present letters
    for i in range(5):
        if feedback[i] == 'correct':
            continue
        if guess[i] in secret_temp:
            feedback[i] = 'present'
            j = secret_temp.index(guess[i])
            secret_temp[j] = None     # Mark as read again for present
    return feedback

def display_feedback(guess, feedback):
    symbols = {'correct': '🟩', 'present': '🟨', 'absent': '⬜'}
    res = ""
    for i in range(5):
        res += f"{guess[i].upper()}{symbols[feedback[i]]} "
    print(res)
    print()  # Spacing for spacing

# Main game function
def play_game(secret_word):
    attempts = 6

    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts. Good luck!🍀")
    print()

    # Loop for attempts
    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt} of {attempts}")

        # get guess from user
        while True:
            g = input("Enter your guess (5-letter word): ").strip().lower()
            if len(g) != 5:
                print("Invalid input! Please enter exactly 5 letters.")
            else:
                break
            
        fb = check_guess(secret_word, g)
        display_feedback(g, fb)
        if g == secret_word:
            print(f"🎉 Congratulations! You've guessed the word correctly in {attempt} attempts.")
            return
    print(f"❌ Out of attempts! The secret word was: {secret_word.upper()}")

# Take off 
# making main function always a good practice
def main():
    secret_word = get_secret_word("words.txt")
    play_game(secret_word)

# When u wanna run the code directly here and if imported somewhere else it won't run directly
if __name__ == "__main__":
    main()