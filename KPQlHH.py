mylist = [(2, 4), (6, 8), (10, 12)]

for tuple in mylist:
    print(tuple)

"""
Output:
(2, 4)
(6, 8)
(10, 12)
"""

# Now with unpacking!
for (t1, t2) in mylist:
    print(t1)

"""
Output:
2
6
10
"""