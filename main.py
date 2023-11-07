input = open('input.txt', 'r')

num_sen = int(input.readline())

with open('input.txt', 'r') as file_in:
    text = file_in.readlines()
words = []

for i in text:
    words.extend(i.split())

words = words[1:]

print(words)

words_dict = {}

for idx in range(len(words)-1):
    words_dict[words[idx]] = words[idx+1]

print(words_dict)