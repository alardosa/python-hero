def check_even(n):
    return n % 2 == 0


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(check_even, nums))
# output: <filter object at 0x00000000021A1D08>

print(list(filter(check_even, nums)))
# output: [0, 2, 4, 6, 8, 10]