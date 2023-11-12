org_str = "Hello World"  # Hello World  --> OLLEh DLROw
new_str = ""
list_of_words = org_str.split(" ")
for word in list_of_words:
    temp = "".join(reversed(word)).swapcase() # swapcase converts "Hello" to "hELLO"
    new_str += temp + " " # this " " is to keep space between each words
print(new_str)


