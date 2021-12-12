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
    Starts the game.
    Validates the user response regarding wanting to play the game.
    """

    plays_game = input("Would you like to play Hangman? < Y or N >: ").upper()
    if plays_game == "Y":
        print("\n")
        print("Let's Play HANGMAN")
        print("\n")
        how_many_letters()
    elif plays_game == "N":
        print("\n")
        print("That is too bad, see ya!")
        print("\n")
    else:
        print("\n")
        print("That isn't a valid response")
        start_game()


def how_many_letters():
    """
    Asks the user if they want to play with three, four, or five letter words.
    Validates the user response of user input is anything other than
    "3", "4" or "5".
    """

    # I need to find a way to shorten line 46 as line is too long.
    letter_amount = input("Would you like to play with 3, 4, 5 letters? < 3, 4, 5 >: ")
    print("\n")

    if letter_amount == "3":
        print("\n")
        print("You selected to play with 3 letters.")
        print("\n")
        three_word_game()
    elif letter_amount == "4":
        print("\n")
        print("You selected to play with 4 letters.")
        print("\n")
        four_word_game()
    elif letter_amount == "5":
        print("\n")
        print("You selected to play with 5 letters")
        print("\n")
        five_word_game()
    else:
        print("\n")
        print("You did not type a valid game amount. Try again")
        how_many_letters()


def three_word_game():
    """
    Will generate a random three letter word for the user to guess.
    Will show blanks to the user for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives or wins the game
    Shows the user a list of already guessed letters.
    Displays each correctly guessed letter in its correct position.
    Displays ascii art of each stage of life the user may, or may not be, at whilst playing the game.
    Asks the user if they would like to play again if they win or lose.
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
        print("\n")    
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
        print("\n")
        print(f"Here is a list of guessed letters: \n {user_guesses}")
        print("\n")

        if user_input not in string.ascii_letters:
            print("\n")
            print(f"{user_input} is invalid. Please enter a letter")
            print("\n")
            user_input = input("Guess a letter: ").upper()
            print("\n")
        elif user_input not in chosen_word:
            lives -= 1
            print("\n")
            print(f"{user_input} is not in the word.")
            print("\n")
            user_guesses.append(user_input)

        if user_input in user_guesses:
            print("\n")
            print(f"Here is a list of guessed letters: \n {user_guesses}")
            print("\n")

            if lives < 6:
                print("\n")
                print(f"You have {lives} lives left")
                print("\n")
                print(f"{hangman_art.hangman_lives[lives]} ")
                print("\n")
            if lives == 0:
                is_game_over = True
                print("\n")
                print("Game Over")
                print("\n")
                start_game()

        if "_" not in display:
            is_game_over = True
            print("\n")
            print("You Win")
            print("\n")
            start_game()


def four_word_game():
    """
    Will show blanks to the user for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives or wins the game
    Shows the user a list of already guessed letters.
    Displays each correctly guessed letter in its correct position.
    Displays ascii art of each stage of life the user may, or may not be, at whilst playing the game.
    Asks the user if they would like to play again if they win or lose.
    """
    chosen_word = random.choice(hangman_words.four_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    user_guesses = []
    lives = 6
    while not is_game_over:
        print("\n")   
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
        print("\n")
        print(f"Here is a list of guessed letters: \n {user_guesses}")
        print("\n")

        if user_input not in string.ascii_letters:
            print("\n")
            print(f"{user_input} is invalid. Please enter a letter")
            print("\n")
            user_input = input("Guess a letter: ").upper()
        elif user_input not in chosen_word:
            lives -= 1
            print("\n")
            print(f"{user_input} is not in the word.")
            print("\n")
            user_guesses.append(user_input)

        if user_input in user_guesses:
            print("\n")
            print(f"Here is a list of guessed letters: \n {user_guesses}")
            print("\n")

            if lives < 6:
                print("\n")
                print(f"You have {lives} lives left")
                print("\n")
                print(f"{hangman_art.hangman_lives[lives]} ")
                print("\n")
            if lives == 0:
                is_game_over = True
                print("\n")
                print("Game Over")
                print("\n")
                start_game()
                
        if "_" not in display:
            is_game_over = True
            print("\n")
            print("You Win")
            print("\n")
            start_game()


def five_word_game():
    """
    Will generate a random three letter word for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives or wins the game
    Shows the user a list of already guessed letters.
    Displays each correctly guessed letter in its correct position.
    Displays ascii art of each stage of life the user may, or may not be, at whilst playing the game.
    Asks the user if they would like to play again if they win or lose.
    """
    chosen_word = random.choice(hangman_words.five_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    user_guesses = []
    lives = 6
    while not is_game_over: 
        print("\n")   
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
        print("\n")
        print(f"Here is a list of guessed letters: \n {user_guesses}")
        print("\n")

        if user_input not in string.ascii_letters:
            print("\n")
            print(f"{user_input} is invalid. Please enter a letter")
            print("\n")
            user_input = input("Guess a letter: ").upper()
            print("\n")
        elif user_input not in chosen_word:
            lives -= 1
            print("\n")
            print(f"{user_input} is not in the word.")
            print("\n")
            user_guesses.append(user_input)

        if user_input in user_guesses:
            print("\n")
            print(f"Here is a list of guessed letters: \n {user_guesses}")
            print("\n")

            if lives < 6:
                print("\n")
                print(f"You have {lives} lives left")
                print("\n")
                print(f"{hangman_art.hangman_lives[lives]} ")
                print("\n")
            if lives == 0:
                is_game_over = True
                print("\n")
                print("Game Over")
                print("\n")
                start_game()
                
        if "_" not in display:
            is_game_over = True
            print("\n")
            print("You Win")
            print("\n")
            start_game()


start_game()



# TO DO LIST

# GAME OVER ASCII ART
# DELETE THE CODE THAT DISPLAYS THE WORD TO THE USER
# A RANDOM WORD AMOUNT GAME AS WELL.
#
# MAYBE CLEAR SCREEN?????
# ASK USER WHAT THEIR NAME IS.
# WRITE COMMENTS ABOUT CODE
# WRITE BETTER FUNCTION DESCRIPTIONS
