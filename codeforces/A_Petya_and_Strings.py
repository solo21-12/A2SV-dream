# Input strings
string1 = input().lower()
string2 = input().lower()

# Perform lexicographical comparison
if string1 < string2:
    print("-1")
elif string1 > string2:
    print("1")
else:
    print("0")
