# adds 10 in any input num
num = lambda n: n + 10
print(num(5))
# output: 15


# a * b
multiplication = lambda a, b: a * b
print(multiplication(2, 2))
# output: 4


addition = lambda a, b, c: a + b + c
print(addition(1, 2, 3))
# output: 6


# reverse string
reverse_string = lambda s: s[::-1]
print(reverse_string('AL ARDOSA'))
# output: ASODRA LA


# Lambda in Functions
def multiply(n):
    return lambda a: a * n

multiply_to = multiply(2)
print(multiply_to(11))
# output: 22


def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
# output: 22
# output: 33


# square root
nums = [1, 2, 3, 4, 5, 8]
square_root = list(map(lambda n: n ** 2, nums))
print(square_root)
# output: [1, 4, 9, 16, 25, 64]


# can be divide by 2
can_divide_by_2 = list(filter(lambda n: n % 2 == 0, nums))
print(can_divide_by_2)
# output: [2, 4, 8]