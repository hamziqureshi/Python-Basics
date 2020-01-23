'''
#----------------------------------------#
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.
'''

class Person:
    name = "Person"

    def __init__(self,name=None):
        self.name = name

a = Person("Hamza")
print("{} name is {}".format(Person.name, a.name))

