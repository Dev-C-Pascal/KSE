import words_fetcher
import random


def setting_up():
    letters_count = 5
    tries_c = 5
    words = words_fetcher.fetch_words(min_letters=letters_count, max_letters=letters_count)
    print(words)

    random_word = random.choice(words)
    print(random_word)

    return random_word, tries_c, words


def check_for_right(dict_word, tries, words):
    check_correct = False
    while (not check_correct) and tries > 0:
        input_word = input("Введіть ваше слово: ")
        if len(input_word) != len(dict_word):
            print("Not that value")
        elif input_word not in words:
            print("Scam")
        else:
            input_arr: list = list(input_word)
            dict_arr: list = list(dict_word)
            for i in range(0, len(input_word)):
                if input_arr[i] == dict_arr[i]:
                    print(f'{input_arr[i].upper()}, ', end='')
                elif input_arr[i] in dict_arr:
                    print(f'{input_arr[i]}* ', end='')
                else:
                    print(f'{input_arr[i]}  ', end='')

        if str(input_word) == str(dict_word):
            print("Cong, you won")
            check_correct = True
        else:
            print("Try one more time")
            tries -= 1


    # if input_word == dict_word:
    #     return "You won"
    # elif str(input_word) != words:
    #     return "You lose"
    # else:
    #     for i in input_word:
    #         if i in dict_word:
    #             new_str += i + "*"
    #     return new_str


random_word, tries_count, dict = setting_up()
print(check_for_right(random_word, tries_count, dict))
