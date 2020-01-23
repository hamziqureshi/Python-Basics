#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS

x = input('Enter sentence:')
dic = {"letters":0,"digits":0}
for i in x:
    if (i.isdigit()):
        dic["digits"]+=1
    elif (i.isalpha()):
        dic["letters"]+=1
    else:
        pass
print("LETTERS",dic["letters"])
print("DIGITS",dic["digits"])
