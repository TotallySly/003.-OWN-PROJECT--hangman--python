import random
import string
import hangman_words
import hangman_art


print(f"{hangman_art.logo}\n")
print("Hello and welcome to the classic game of Hangman.")
print("The rules of the game are simple.")
print("Guess the word before the man is hanged.")
print("\n")


def start_game():
    """
    Starts the game and asks the user what they would like to be called.
    Validates the user response regarding wanting to play the game.
    """

    plays_game = input("Would you like to play Hangman? < Y or N >: ").upper()
    if plays_game == "Y":
        print("\n")
        print("Let's Play HANGMAN")
        print("\n")
        how_many_letters()
    elif plays_game == "N":
        print("That is too bad, see ya!")
    else:
        print("That isn't a valid response")
        start_game()


def how_many_letters():
    """
    Asks the user if they want to play with three, four, or five letter words.
    Validates the user response of user input is anything other than
    "3", "4" or "5".
    """
    # I need to find a way to shorten line 46 as line is too long.
    letter_amount = input("Would you like to play with 3, 4 or 5 letters? < 3, 4, 5 >: ")
    print("\n")

    if letter_amount == "3":
        print("You selected to play with 3 letters.")
        print("\n")
        three_word_game()
    elif letter_amount == "4":
        print("You selected to play with 4 letters.")
        print("\n")
        four_word_game()
    elif letter_amount == "5":
        print("\n")
        print("You selected to play with 5 letters")
        five_word_game()
    else:
        print("You did not type a valid game amount. Try again")
        how_many_letters()


def three_word_game():
    """
    Will generate a random three letter word for the user to guess.
    Will show blanks to the user for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives.
    """
    chosen_word = random.choice(hangman_words.three_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    user_guesses = []
    lives = 6
    while not is_game_over:    
        user_input = input("Guess a letter: ").upper()
        print("\n")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_input:
                display[position] = letter
        print(display)
        print("\n")
        print(f"You have {lives} lives left")
        print("\n")
        print(f"{hangman_art.hangman_lives[lives]} ")

        if user_input not in string.ascii_letters:
            print(f"{user_input} is invalid. Please enter a letter")
            user_input = input("Guess a letter: ").upper()
            
        if user_input not in chosen_word:
            lives -= 1
            user_guesses.append(user_input)
            
        if user_input in user_guesses:
            print("\n")
            print(f"Here is a list of guessed letters: \n {user_guesses}")
            print("\n")

            if lives < 6:
                print(f"You have {lives} lives left")
                print(f"{hangman_art.hangman_lives[lives]} ")
            if lives == 0:
                is_game_over = True
                print("Game Over")
        if "_" not in display:
            is_game_over = True
            print("You Win")


def four_word_game():
    """
    Will generate a random four letter word for the user to guess.
    Will show blanks to the user for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives.
    """
    chosen_word = random.choice(hangman_words.three_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    user_guesses = []
    lives = 6
    while not is_game_over:    
        user_input = input("Guess a letter: ").upper()
        print("\n")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_input:
                display[position] = letter
        print(display)
        print("\n")
        print(f"You have {lives} lives left")
        print("\n")
        print(f"{hangman_art.hangman_lives[lives]} ")

        if user_input not in string.ascii_letters:
            print(f"{user_input} is invalid. Please enter a letter")
            user_input = input("Guess a letter: ").upper()
            
        if user_input not in chosen_word:
            lives -= 1
            user_guesses.append(user_input)
            
        if user_input in user_guesses:
            print("\n")
            print(f"Here is a list of guessed letters: \n {user_guesses}")
            print("\n")

            if lives < 6:
                print(f"You have {lives} lives left")
                print(f"{hangman_art.hangman_lives[lives]} ")
            if lives == 0:
                is_game_over = True
                print("Game Over")
        if "_" not in display:
            is_game_over = True
            print("You Win")


def five_word_game():
        """
    Will generate a random three letter word for the user to guess.
    Will show blanks to the user for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives.
    """
    chosen_word = random.choice(hangman_words.three_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    user_guesses = []
    lives = 6
    while not is_game_over:    
        user_input = input("Guess a letter: ").upper()
        print("\n")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_input:
                display[position] = letter
        print(display)
        print("\n")
        print(f"You have {lives} lives left")
        print("\n")
        print(f"{hangman_art.hangman_lives[lives]} ")

        if user_input not in string.ascii_letters:
            print(f"{user_input} is invalid. Please enter a letter")
            user_input = input("Guess a letter: ").upper()
            
        if user_input not in chosen_word:
            lives -= 1
            user_guesses.append(user_input)
            
        if user_input in user_guesses:
            print("\n")
            print(f"Here is a list of guessed letters: \n {user_guesses}")
            print("\n")

            if lives < 6:
                print(f"You have {lives} lives left")
                print(f"{hangman_art.hangman_lives[lives]} ")
            if lives == 0:
                is_game_over = True
                print("Game Over")
        if "_" not in display:
            is_game_over = True
            print("You Win")
 
start_game()