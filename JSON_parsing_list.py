import json
data = '''[
{"id" : "001",
 "x" : "2",
 "name" : "Chuck"
 } ,
 { "id" : "009",
 "x" : "7",
 "name" : "Hamza"
 }
]'''

info = json.loads(data)
print("User count:",len(info))
for item in info:
    print('Name:',item["name"])
    print('ID:',item["id"])
    print('Attributes:',item['x'])
