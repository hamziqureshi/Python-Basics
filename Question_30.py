'''
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only. 
'''

a = input("Enter email:")

b = a.find("@")
c = a.find(".")
print("Username:",a[:b])
print("Coompany name:",a[b+1:c])
