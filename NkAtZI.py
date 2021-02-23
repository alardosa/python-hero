print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
# output: The quick brown fox

print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=11.3))
# output: First Object: 1, Second Object: Two, Third Object: 11.3

print('A %s saved is a %s earned.' %('penny','penny'))
# output: A penny saved is a penny earned.

print('A {p} saved is a {p} earned.'.format(p='penny'))
# output: A penny saved is a penny earned.
# output: A penny saved is a penny earned.

print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))
# output: The fox fox fox

result = 100/777
print("The result was {r}".format(r=result))
# output: The result was 0.1287001287001287

print("The result was {r:1.5f}".format(r=result))
# output: The result was 0.12870

# round the result
result = 100/777
print("The result was {r:1.2f}".format(r=result))
# output: The result was 0.13

# two-decimal number
result = 104.12345
print("The result was {r:1.2f}".format(r=result))
# output: The result was 104.12

name = 'Sam'
age = 3
print(f'{name} is {age} years old.')
# output: Sam is 3 years old.