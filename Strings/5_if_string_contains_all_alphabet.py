import string

s = "The quick brown fox jumps over the lazy dog !135"
flag = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        flag = False
        break # Stop the loop immediately as we got a False case already

print(flag)
