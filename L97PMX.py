index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

print('-----------------------------------------------------------------')

"""
Output:
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e
-----------------------------------------------------------------
"""

# tuple unpacking!
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

"""
Output:
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e
"""