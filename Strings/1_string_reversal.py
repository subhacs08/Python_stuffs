# option 1
org_str = "Hello" # Hello
print(org_str)    # 01234
l = len(org_str)
# print(org_str[4]+org_str[3]+org_str[2]+org_str[1]+org_str[0])
# print(org_str[-1]) # -1 --> last index --> o
rev_str1 = org_str[-1:-6:-1]
rev_str2 = org_str[-1:-(l+1):-1]
rev_str3 = org_str[::-1]
print(rev_str1, rev_str2, rev_str3)
# 4 3 2 1 0
# H e l l o
#-5-4-3-2-1


# option 2

org_str = "HelloWorld"
revv_str = reversed(org_str)
print(revv_str)  # <reversed object at 0x0000018663B97310>
# print(next(revv_str))
final_str = "".join(revv_str)
print(final_str)
