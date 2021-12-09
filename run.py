import random
import hangman_words
import hangman_art


chosen_4_letter_word = random.choice(hangman_words.four_letter_words)
chosen_5_letter_word = random.choice(hangman_words.five_letter_words)


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
        how_many()
    elif plays_game == "N":
        print("That is too bad, see ya!")
    else:
        print("That isn't a valid response")
        start_game()

# Maybe change function to play game? A lot of functions could be added to IF
def how_many():
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
        random_3_word()
        # Function to show ___ to the user....
    elif letter_amount == "4":
        print("You selected to play with 4 letters.")
        print("\n")
        random_4_word()
        # Function to show ____ to the user....
    elif letter_amount == "5":
        print("\n")
        print("You selected to play with 5 letters")
        random_5_word()
        # Function to show ____ to the user....
    else:
        print("You did not type a valid game amount. Try again")
        how_many()


def random_3_word():
    """
    Will generate a random three letter word for the user to guess.
    """
    chosen_word = random.choice(hangman_words.three_letter_words)
    print(chosen_word)
    show_blanks = []
    for letter in chosen_word:
        show_blanks += "_"
    print(show_blanks)


def random_4_word():
    """
    Will generate a random four letter word for the user to guess.
    """
    chosen_word = random.choice(hangman_words.four_letter_words)
    print(chosen_word)
    show_blanks = []
    for letter in chosen_word:
        show_blanks += "_"
    print(show_blanks)


def random_5_word():
    """
    Will generate a random five letter word for the user to guess.
    """
    chosen_word = random.choice(hangman_words.five_letter_words)
    print(chosen_word)
    show_blanks = []
    for letter in chosen_word:
        show_blanks += "_"
    print(show_blanks)


# def show_blanks():
#     show_blanks = []
#     for letter in chosen_word:
#         show_blanks += "_"
#     print(show_blanks)


# show_blanks()
start_game()
