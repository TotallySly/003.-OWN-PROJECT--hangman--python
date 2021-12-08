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


def start_game():
    """
    Starts the game and asks the user what they would like to be called
    """

    plays_game = input("Would you like to play Hangman? <Y or N>: ").upper()
    if plays_game == "Y":
        print("Let's Play HANGMAN")
        # TAKE USER TO HANGMAN GAME
    elif plays_game == "N":
        print("That is too bad, see ya!")
    else:
        print("That isn't a valid response")
        start_game()



def how_many():
    """
    Asks the user if they want to play with three, four, or five letter words.
    """

    input("")



start_game()
