#----------------------------------------#
#Question 6
#Level 2

#Question:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
import math 
x = input("Enter sequence:")
x = x.split(",")
C = 50
H = 30
def Formula(C,D,H):
    return math.sqrt((2*C*D)/H)

y = list()
for i in range(0,len(x)):
    y.append(int(Formula(C,int(x[i]),H)))
    
print(y)
#there answer
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
