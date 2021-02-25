# def my_func(n):
#     result = n + 2
#     return result
#
#
# try:
#     my_func(2)
#
# except:
#     print('Not Added Correctly!')
#
# else:
#     print('Added Correctly!')
#     print(my_func(2))
# -----------------------------------------------------------------------------------

# try:
#     f = open("testfile", "w")
#     f.write("Test write statement")
#     f.close()
# finally:
#     print("Always execute finally code blocks")

# try:
#     val = int(input("Please enter an integer: "))
# except:
#     print("Looks like you did not enter an integer!")
# finally:
#     print("Finally, I executed!")
# -----------------------------------------------------------------------------------


def ask_int():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except IOError:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")
        print(val)


ask_int()
