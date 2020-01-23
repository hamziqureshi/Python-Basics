Open = open("abc.txt")
Read = Open.read()
List = Read.split()

dic = dict()
for word in List:
    dic[word] = dic.get(word,0)+1

print(sorted([(val,key) for key,val in dic.items()],reverse = True))
