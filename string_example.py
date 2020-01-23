x = "From hamzaakramqureshi@gmail.com Sat Jan 5 09:14:16 2019"

name_start = x.find(" ")
company_start = name_end = x.find("@")
print(x[name_start+1:name_end])
company_end = x.find(".",company_start)
print(x[company_start+1:company_end])
