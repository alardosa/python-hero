print("I'm going to inject %s here." %'something')
# output: I'm going to inject something here.

print("I'm going to inject %s text here, and %s text here." %('some','more'))
# output: I'm going to inject some text here, and more text here.

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))
# output: I'm going to inject some text here, and more text here.