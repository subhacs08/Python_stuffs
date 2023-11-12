# Option 1
org_str = "Python"
new_str = org_str[1::2]
print(new_str)

# Option 2
orgg_str = "Python"
neww_str = ""
for i in range(len(orgg_str)):
    if i % 2 != 0:
        neww_str += orgg_str[i]
print(neww_str)
