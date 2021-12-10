import random
import string
import hangman_words
import hangman_art






# print(chosen_4_letter_word)
# print(chosen_5_letter_word)


print(f"{hangman_art.logo}\n")
print("Hello and welcome to the classic game of Hangman.")
print("The rules of the game are simple.")
print("Guess the word before the man is hanged.")
print("\n")

# Maybe require a while loop for playing the game????
# While game_over = false, play the game????


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


# Maybe change function to play game? A lot of functions could be added to IF
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
        # Function to show ___ to the user....
    elif letter_amount == "4":
        print("You selected to play with 4 letters.")
        print("\n")
        four_word_game()
        # Function to show ____ to the user....
    elif letter_amount == "5":
        print("\n")
        print("You selected to play with 5 letters")
        five_letter_game()
        # Function to show ____ to the user....
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
    lives = 6
    while not is_game_over:    
        user_input = input("Guess a letter: ").upper()
        print(user_input)

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_input:
                display[position] = letter
        print(display)

        if user_input not in string.ascii_letters:
            print(f"{user_input} is invalid. Please enter a letter")
            user_input = input("Guess a letter: ").upper()
        if user_input not in chosen_word:
            lives -= 1
            print(lives)
            if lives < 6:
                print(f"You have {lives} left") # ASCII ART HERE. F STRING LIVES AMOUNT
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
    chosen_word = random.choice(hangman_words.four_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    lives = 6
    while not is_game_over:   
        user_input = input("Guess a letter: ").upper()
        print(user_input)

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_input:
                display[position] = letter
        print(display)

        if user_input not in string.ascii_letters:
            print(f"{user_input} is invalid. Please enter a letter")
            user_input = input("Guess a letter: ").upper()
        if user_input not in chosen_word:
            lives -= 1
            print(lives)
            if lives == 0:
                is_game_over = True
                print("Game Over")
        if "_" not in display:
            is_game_over = True
            print("You Win")


def five_word_game():
    """
    Will generate a random five letter word for the user to guess.
    Will show blanks to the user for the user to guess.
    Checks the if user input is valid using ascii characters.
    While loop whilst game is not over, until the user loses all lives.
    """
    chosen_word = random.choice(hangman_words.five_letter_words).upper()
    print(chosen_word)

    display = []
    for letter in chosen_word:
        display += "_"

    is_game_over = False
    lives = 6
    while not is_game_over: 
        user_input = input("Guess a letter: ").upper()
        print(user_input)

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_input:
                display[position] = letter
        print(display)

        if user_input not in string.ascii_letters:
            print(f"{user_input} is invalid. Please enter a letter")
            user_input = input("Guess a letter: ").upper()
        if user_input not in chosen_word:
            lives -= 1
            print(lives)
            if lives == 0:
                is_game_over = True
                print("Game Over")
        if "_" not in display:
            is_game_over = True
            print("You Win")




start_game()