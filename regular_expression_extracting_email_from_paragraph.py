import re
x = "From hamzaakramqureshi@gmail.com Sat Jan 5 09:14:16 2019"
y = re.findall("\S+@\S+",x)
y = str(y)
z = y.split("@")
name = z[0]
com = z[1].split(".")
company = com[0]
print(name)
print(company)
