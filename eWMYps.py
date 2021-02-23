def square(n):
    return n ** 2


my_list = [1, 2, 3, 4, 5]

print(map(square, my_list))
# output: <map object at 0x00000000022B1CC8>

print(list(map(square, my_list)))
# output: [1, 4, 9, 16, 25]