x = 0
while x < 5:
    print(f'x is currently: {x}')
    print(' x is still less than 5, adding 1 to x')
    x += 1
    if x == 3:
        print('x==3')
    else:
        print('continuing...')
        continue

"""
Output:
x is currently:  0
 x is still less than 5, adding 1 to x
continuing...
x is currently:  1
 x is still less than 5, adding 1 to x
continuing...
x is currently:  2
 x is still less than 5, adding 1 to x
x==3
x is currently:  3
 x is still less than 5, adding 1 to x
continuing...
x is currently:  4
 x is still less than 5, adding 1 to x
continuing...
"""

print('---------------------------------------------')

# put in a break once y ==3 and see if the result makes sense:
y = 0
while y < 10:
    print(f'y is currently: {y}')
    print(' y is still less than 10, adding 1 to y')
    y += 1
    if y == 3:
        print('Breaking because y==3')
        break
    else:
        print('continuing...')
        continue

"""
Output:
y is currently:  0
 y is still less than 10, adding 1 to y
continuing...
y is currently:  1
 y is still less than 10, adding 1 to y
continuing...
y is currently:  2
 y is still less than 10, adding 1 to y
Breaking because y==3
"""