lc = [x for x in range(11) if x % 2 == 0]
print(lc)
# output: [0, 2, 4, 6, 8, 10]

#or

lc = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(lc)
# output: [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]