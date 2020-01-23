'''
#----------------------------------------#
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance
from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
import math
num = [0,0]
while 1:
    x = input("Enter input:")
    if not x:
        break
    x = x.split(" ")
    a = x[0]
    n = int(x[1])
    if a == "UP":
        num[0] += n
    elif a == "DOWN":
        num[0] -= n
    elif a == "RIGHT":
        num[1] += n
    elif a == "LEFT":
        num[1] -= n
    else:
        pass
print(num)
print(int(round(math.sqrt(num[0]**2+num[1]**2))))
