dic = {0:"7",1:"8",2:"9",3:"10",4:"J",5:"Q",6:"K",7:"A"}
lst = [5,3,0,7]

for i in lst:
    for key,val in enumerate(lst):
        lst[key] = dic.get(val,val)

print(lst)
