print(len('abcd efgh'))
# output: 9

mystring = 'abcd efgh'
print(mystring)
# output: abcd efgh

mystring = 'abcdefghijk'
print(mystring[0])
# output: a

print(mystring[1])
# output: b

# get last letter
print(mystring[-1])
# output: k

# remove last letter
print(mystring[:-1])
# output: abcdefghij

print(mystring[-2])
# output: j

print(mystring[2:])
# output: cdefghijk

print(mystring[:2])
# output: ab

print(mystring[2:5])
# output: cde

print(mystring[1:3])
# output: bc

print(mystring[::2])
# output: acegik

print(mystring[::3])
# output: adgj

# print a string backwards
print(mystring[::-1])
# output: kjihgfedcba