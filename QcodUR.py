celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]
print(fahrenheit)
# output: [32.0, 50.0, 68.18, 94.1]

lc = [x ** 2 for x in [x ** 2 for x in range(11)]]
print(lc)
# output: [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]