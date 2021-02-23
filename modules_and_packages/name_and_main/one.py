def func_one():
    print("one_func() function ran in one.py")


def func_two():
    pass


def func_three():
    pass


print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")

    # YOU CAN RUN SCRIPT HERE!
    func_two()
    func_three()

else:
    print("one.py is being imported into another module")