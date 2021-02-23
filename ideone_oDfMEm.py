n = 25


def func():
    global n
    print('This function is now using the global n!')
    print(f'Because of global n is: {n}')
    n = 2
    print(f'Ran func(), changed global n to, {n}')


print(f'Before calling func(), n is: {n}')
func()
print(f'Value of n outside of func() is: {n}')

"""
Output:
Before calling func(), n is:  25
This function is now using the global n!
Because of global n is:  25
Ran func(), changed global n to 2
Value of n outside of func() is:  2
"""