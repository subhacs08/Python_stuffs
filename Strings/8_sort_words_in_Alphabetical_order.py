org_str = "Hello World" # Hello World --> OLLEh DLROw
list_of_words = org_str.split(" ")
new_str = ""

for word in list_of_words:
    new_str += "".join(sorted(word)) + " "

print(new_str)
