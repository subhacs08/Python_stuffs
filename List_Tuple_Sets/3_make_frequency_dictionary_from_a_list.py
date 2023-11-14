my_list = ["a", "b", "c", "a"]
freq_dict = {}

for item in my_list:
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1

print(freq_dict)
