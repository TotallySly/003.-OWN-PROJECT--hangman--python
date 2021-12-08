import random
import hangman_words


word_list = ["bye", "hello", "four"]

chosen_3_letter_word = random.choice(hangman_words.three_letter_words)
chosen_4_letter_word = random.choice(hangman_words.four_letter_words)
chosen_5_letter_word = random.choice(hangman_words.five_letter_words)

print(chosen_3_letter_word)
print(chosen_4_letter_word)
print(chosen_5_letter_word)

