import re
x = "From hamzaakramqureshi@gmail.com Sat Jan 5 09:14:16 2019"
z = re.findall("\S+@\S+",x)
y = str(z[0])
name = re.findall("^([^@]*)",y)
company = re.findall("^.*@([^.]*)",y)
print(name)
print(company)
