import random
import hangman_words
import hangman_art

word_list = ["bye", "hello", "four"]

chosen_3_letter_word = random.choice(hangman_words.three_letter_words)
chosen_4_letter_word = random.choice(hangman_words.four_letter_words)
chosen_5_letter_word = random.choice(hangman_words.five_letter_words)

# print(chosen_3_letter_word)
# print(chosen_4_letter_word)
# print(chosen_5_letter_word)


print(f"{hangman_art.logo}\n")
print("Hello and welcome to the classic game of Hangman.")
print("The rules of the game are simple.")
print("Guess the word before the man is hanged.")
print("\n")


def start_game():
    """
    Starts the game and asks the user what they would like to be called
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


def how_many():
    """
    Asks the user if they want to play with three, four, or five letter words.
    """

    letter_amount = input("Would you like to play with 3, 4 or 5 letters? < 3, 4, 5 >: ")
    print(type(letter_amount))
    print("\n")

    if letter_amount == "3":
        print("You selected to play with 3 letters.")
    elif letter_amount == "4":
        print("You selected to play with 4 letters.")
    elif letter_amount == "5":
        print("You selected to play with 5 letters")
    else:
        print("You did not type a valid game amount. Try again")
        how_many()


start_game()
