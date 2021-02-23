def myfunc(*args, **kwargs):
    if 'one' and 'two' in kwargs:
        print(f"I like letters {' and '.join(args)} and my numbers is {kwargs['two']}")
        print(f"May I have number {kwargs['one']} one?")
    else:
        pass


myfunc('a', 'b', 'c', one=1, two='Dos')

"""
Output:
I like letters a and b and c and my numbers is Dos
May I have number 1 one?
"""