inputString = input() # Enter Input string

dict_counter = {}  # Dictionary to hold the characters and frequencies

for char in inputString:
    if not dict_counter or char not in dict_counter.keys():
        dict_counter.update({char: 1})
    elif char in dict_counter.keys():
        dict_counter[char] += 1
for key, val in dict_counter.items():
    print(key, val)


    