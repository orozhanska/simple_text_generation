import random
from module_tokens import tokens_dict

counter = 0
key = random.choice(list(tokens_dict.keys()))
print(key.capitalize(), end=' ')
while counter != 200:
    if key == '.':
        capital = True
    else:
        capital = False
    key = random.choice(tokens_dict[key])
    if key in '.,;:':
        print(key, end=' ')
    elif key == "'":
        print(key, end='')
    else:
        if capital:
            print(key.capitalize(), end=' ')
        else:
            print(key, end=' ')
    counter += 1
