print('This is a string {}'.format('INSERTED'))
# output: This is a string INSERTED

print('The {} {} {}'.format('fox', 'brown', 'quick'))
# output: The fox brown quick

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# output: The quick brown fox

print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
# output: The fox fox fox