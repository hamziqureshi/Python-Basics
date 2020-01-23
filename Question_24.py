'''
#----------------------------------------#
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it,
    you can read document online or find some books.
    But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
'''

def sq(n):
    '''Calculate the square of the input number'''
    return n**2

print(sq(2))
print(sq.__doc__)
