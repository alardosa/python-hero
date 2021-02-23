mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Start sum at zero
mysum = 0

for mynum in mylist:
    mysum = mysum + mynum

print(mysum)

# output: 55


# Start sum at zero
mysum = 0

for mynum in mylist:

    # you can also use +=
    mysum += mynum

print(mysum)
# output: 55