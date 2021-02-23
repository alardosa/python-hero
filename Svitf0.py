print(list(enumerate('abcde')))

"""
Output:
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
"""
print('-----------------------------------------------------------------')

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']

print(zip(mylist1, mylist2))

"""
Output:
<zip object at 0x0000000002821D08>
"""
print('-----------------------------------------------------------------')

print(list(zip(mylist1,mylist2)))

"""
Output:
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
"""
print('-----------------------------------------------------------------')

for item1, item2 in zip(mylist1, mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1, item2))

"""
Output:
For this tuple, first item was 1 and second item was a
For this tuple, first item was 2 and second item was b
For this tuple, first item was 3 and second item was c
For this tuple, first item was 4 and second item was d
For this tuple, first item was 5 and second item was e
"""