'''
Question:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
'''

def gen(n):
    lst = list()
    for i in range(n):
        if (i%7==0):
            lst.append(i)
    return lst

gen()
