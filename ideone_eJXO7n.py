def say_hi():
    # Enclosing function
    name = 'Al Ardosa'

    def hi():
        print('Hi ' + name, 'How are you?')

    hi()


say_hi()
# output: Hi Al Ardosa How are you?