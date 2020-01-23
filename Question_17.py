#Question 17
#Level 2

#Question:
#Write a program that computes the net amount of a bank account based a transaction log from console input.
#The transaction log format is shown as following:
#D 100
#W 200

#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500
D = int()
while 1:
    x = input("Enter D or W:")
    if not x:
        break
    val = x.split(' ')
    a = val[0]
    b = int(val[1])
    if a == "D":
        D += b
    elif a == "W":
        D -= b


