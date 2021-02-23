d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

print('-----------------')
print(d.items())
print('-----------------')

# Dictionary unpacking
for key, value in d.items():
    print(key)
    print(value)

print('-----------------')
print(list(d.keys()))
print('-----------------')

print(sorted(d.values()))

"""
Output:
k1
k2
k3
-----------------
dict_items([('k1', 1), ('k2', 2), ('k3', 3)])
-----------------
k1
1
k2
2
k3
3
-----------------
['k1', 'k2', 'k3']
-----------------
[1, 2, 3]
"""