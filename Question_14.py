#Question 14
#Level 2

#Question:
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

x = input("Enter sentence:")
dic = {"UC":0,"LC":0}
for i in x:
    if (i.isupper()):
        dic["UC"] +=1
    elif (i.islower()):
        dic["LC"] +=1
    else:
        pass

print("UPPER CASE",dic["UC"])
print("LOWER CASE",dic["LC"])
