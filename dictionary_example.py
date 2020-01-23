Open = open("abc.txt")  #Open text file
Read = Open.read()      #Read text file

Text = Read.split()     #create list from text file
#print(List)

dic = dict()            #create dictionary
for word in Text:       #access the list iteratively
    dic[word] = dic.get(word,0)+1 #use get method to count the instance of word in list

bigcount=None
bigword=None
for word,count in dic.items():
    if bigcount is None or count>bigcount:
        bigcount = count
        bigword = word

print(bigword,bigcount)
    
