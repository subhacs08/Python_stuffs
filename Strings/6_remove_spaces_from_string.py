# Option 1
org_str = "Hello World!"
final_str = ""

for char in org_str:
    if char != " ":
        final_str += char
print(final_str)

# Option 2
print(org_str.replace(" ", ""))  # This approach is better as we are not using any extra variable

