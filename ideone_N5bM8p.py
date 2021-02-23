# This is global
n = 25


def func(n):
    # calling global value
    print(f'n is, {n}')

    # assigning new local
    n = 14
    print(f'Changed global n to, {n}')


# This is local variable n call
func(n)

# This is global variable n call
print('n is still', n)


"""
Output:
n is 25
Changed global n to 14
n is still 25
"""