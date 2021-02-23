FULL_NAME = 'Al Ardosa'


def hello(name):
    print(f'Hello {name}, The hello() function has been executed')

    def hi_func():
        return '\t This is inside the hi_func() function'

    def how_are_you():
        return "\t This is inside the how_are_you() function"

    print(hi_func())
    print(how_are_you())
    print("Now we are back inside the hello() function")


hello(FULL_NAME)

"""
Output:
Hello Al Ardosa, The hello() function has been executed
	 This is inside the hi_func() function
	 This is inside the how_are_you() function
Now we are back inside the hello() function
"""
print('-----------------------------------------------------------------')

def hello_new():
    return 'Hi Al!'


def other(func):
    print('Other code would go here')
    print(func())


other(hello_new)
"""
Output:
Other code would go here
Hi Al!
"""
print('-----------------------------------------------------------------')

def new_decorator(func):
    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func


@new_decorator  # This is your on/off switch
def func_needs_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator()

print('-----------------------------------------------------------------')
# or

ASSIGNED_FUNC = new_decorator(func_needs_decorator)

ASSIGNED_FUNC()

"""
Output:
Code would be here, before executing the func
This function is in need of a Decorator
Code here will execute after the func()
"""