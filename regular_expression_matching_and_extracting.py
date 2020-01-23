import re
x = "my 2 numbers are 39 and 64"
y = re.findall("[0-9]+",x)
print(y)
