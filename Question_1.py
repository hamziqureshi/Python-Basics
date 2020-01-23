#----------------------------------------#
#Question 1
#Level 1

#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

#Hints: 
#Consider use range(#begin, #end) method


start = int("2000")
end = int("3200")

ans=list()
for i in range(start,end+1):
    if (i%7==0) and (i%5!=0):
        ans.append(str(i))
        
print(ans)
