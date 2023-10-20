import words_fetcher
import random


def setting_up():
    letters_count = 6
    tries_c = 8
    words = words_fetcher.fetch_words(min_letters=letters_count, max_letters=letters_count)
    print(words)

    random_word = random.choice(words)
    print(random_word)

    return random_word, tries_c, words, letters_count

random_word, tries_count, dict, word_len = setting_up()

def hangnman(r_word, tries_count, word_len):
    r_word = list(r_word)
    secret_word = []

    for i in range(word_len):
        secret_word.append("*")

    while tries_count >= 0:
        if secret_word == r_word:
            return "you won"
        letter = input("Введіть вашу букву: ")
        if letter in r_word:
            for i in range(len(secret_word)):
                if letter == r_word[i]:
                    secret_word[i] = letter
            print(secret_word)

        else:
            tries_count -= 1
            print(f"{secret_word}, you have {tries_count} mistakes left")
    return "you lose"

print(hangnman(random_word, tries_count,word_len))


