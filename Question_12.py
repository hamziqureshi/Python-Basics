#Question 12
#Level 2

#Question:
#Write a program, which will find all such numbers between 1000 and 3000
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.
val = list()
for i in range(1000,3001):
    c = str(i)
    if ((int(c[0])%2 == 0) and (int(c[1])%2 == 0) and (int(c[2])%2 == 0) and (int(c[3])%2 == 0)):
        val.append(i)
print(val)
