import xml.etree.ElementTree as ET
data = '''<person>
<name>Hamza Akram</name>
<phone type = "intl">
 +1 734 303 4456
 </phone>
 <email hide = "hamzaakramqureshi@gmail.com"/>
 </person>'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
