# Option 1
org_str = "Hello"
new_str = ""

curr_char = "l"
new_char = "s"

for char in org_str:
    if char == curr_char:
        new_str += new_char
    else:
        new_str += char

print(new_str)

# Option 2
org_str = "Hello"

curr_char = "l"
new_char = "s"

print(org_str.replace(curr_char, new_char))
