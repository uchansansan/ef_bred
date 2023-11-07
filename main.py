input = open('input.txt', 'r', encoding='utf-8')

num_sen = int(input.readline())

with open('input.txt', 'r', encoding='utf-8') as file_in:
    text = file_in.readlines()
words = []

for i in text:
    words.extend(i.split())

words = words[1:]


words_dict = {}

for idx in range(len(words)-1):
    if words[idx] in words_dict.keys():
        words_dict[words[idx]] += [words[idx+1]]
    else:
        words_dict[words[idx]] = [words[idx + 1]]

print(words_dict)

