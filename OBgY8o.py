print(range(0,11))
#output: range(0,11)

# 11 is not included, up to but not including 11
print(list(range(0,11)))
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('-----------------------------------------------------------------')

# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
# take from the starting number to get to the next number.
print(list(range(0,11,2)))
# output: [0, 2, 4, 6, 8, 10]
print('-----------------------------------------------------------------')

print(list(range(0,101,10)))
#output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('-----------------------------------------------------------------')