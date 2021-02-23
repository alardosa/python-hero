# print only the even numbers from that list!
# % is modulo to get the remainder only
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for mynum in mylist:
    if mynum % 2 == 0:
        print('Even Number', mynum)
    else:
        print(f'Odd number: {mynum}')

"""
Output:
Odd number: 1
Even Number 2
Odd number: 3
Even Number 4
Odd number: 5
Even Number 6
Odd number: 7
Even Number 8
Odd number: 9
Even Number 10
"""