#Question 15
#Level 2

#Question:
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program: 9
#Then, the output should be:
#11106

x  = input("Enter number:")
a1 = int(x)
a2 = int("%s%s" % (x,x))
a3 = int("%s%s%s" % (x,x,x))
a4 = int("%s%s%s%s" % (x,x,x,x))
A = a1+a2+a3+a4
print(A)

    
