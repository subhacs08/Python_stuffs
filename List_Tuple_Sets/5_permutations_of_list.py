import itertools
my_list = [1,2,3,4,5]

all_permutations = itertools.permutations(my_list)

for items in all_permutations:
    print(items)

