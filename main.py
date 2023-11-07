import random
def list_keys_upper(keys):
    key_list_upper = []
    for key in keys:
        if key[0].isupper():
            key_list_upper.append(key)
    return key_list_upper

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
result = ''
for i in range(num_sen):
    out = ''
    first_word_list = list_keys_upper(words_dict.keys())
    n = len(first_word_list)
    #print(n)
    #print(random.randint(0, n))
    start = first_word_list[random.randint(0, n-1)]
    out += start + ' '
    for j in range(10):
        #print(len(words_dict[start]), words_dict[start])
        m = random.randint(0, len(words_dict[start])-1)
        out += words_dict[start][m] + ' '
        start = words_dict[start][m]
    print(out+'.')
    #print(first_word_list[random.randint(0, n-1)])
    #print(list_keys_upper(words_dict.keys())[random.randint(0, n-1)])
