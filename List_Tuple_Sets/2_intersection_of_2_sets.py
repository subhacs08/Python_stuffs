set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 = {4,5,6,17,18,19}

# Option 1
intersection_set = set()

for ele in set1:
    if ele in set2:
        intersection_set.add(ele)

print(intersection_set)

# Option 2

print(set1.intersection(set2))

# Option 3

print(set1.intersection(set2, set3))
