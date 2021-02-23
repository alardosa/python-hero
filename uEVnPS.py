mystring = ' abcd efgh'
mystring = mystring + ' concatenate me!'
# upper case the string
print(mystring.upper())
# output: ABCD EFGH CONCATENATE ME!

# lower case the string
mystring = ' ABCD EFGH'
mystring = mystring + ' concatenate me!'
print(mystring.lower())
# output: abcd efgh concatenate me!

# split string and remove a specific element
mystring = 'Hello World'
mystring = mystring + ' concatenate me!'
print(mystring.split('W'))
# output: ['Hello ', 'orld concatenate me!']