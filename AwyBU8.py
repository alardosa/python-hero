def intro(**data):
    print("\nData type of argument:", type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Al", Lastname="Ardosa", Age=30, Phone=1234567890)
intro(Firstname="Python", Lastname="Master", Website='https://www.alardosa.com', Country="Philippines", Linkedin="linkedin.com/in/alardosa/", Phone='+63 920 4045 888')

"""
Output:
Data type of argument: <class 'dict'>
Firstname is Al
Lastname is Ardosa
Age is 30
Phone is 1234567890

Data type of argument: <class 'dict'>
Firstname is Python
Lastname is Master
Website is https://www.alardosa.com
Country is Philippines
Linkedin is linkedin.com/in/alardosa/
Phone is +63 920 4045 888
"""