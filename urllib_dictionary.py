import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
dic = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
print(dic)
