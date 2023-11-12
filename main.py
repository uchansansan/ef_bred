"""
Case_4
Group:
Uchanov Igor        80%
Fishchukova Sofia   45%
Tsvykh Viktoria     45%
"""

import random


def extract_upper_case_keys(keys):
    upper_case_keys = [key for key in keys if key[0].isupper()]
    return upper_case_keys


def main():
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        num_sentences = int(file_in.readline())
        text = file_in.readlines()

    words = [word for line in text for word in line.split()][1:]

    word_dict = {}
    for idx in range(len(words) - 1):
        if words[idx] in word_dict:
            word_dict[words[idx]].append(words[idx + 1])
        else:
            word_dict[words[idx]] = [words[idx + 1]]

    for _ in range(num_sentences):
        output = ''
        first_words = extract_upper_case_keys(word_dict.keys())
        n = len(first_words)
        start = first_words[random.randint(0, n - 1)]
        output += start + ' '

        for _ in range(10):
            if start in word_dict:
                choices = word_dict[start]
                next_word = random.choice(choices)
                output += next_word + ' '
                start = next_word
            else:
                break

        print(output.strip() + '.')


if __name__ == "__main__":
    main()
