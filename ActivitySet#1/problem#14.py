# Using Web Services
# https://www.py4e.com/lessons/servces

# XML And Tree
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

URL = 'http://py4e-data.dr-chuck.net/comments_1548413.xml'

fhand = urllib.request.urlopen(URL)

xml_data =''''''

for line in fhand:
  xml_data += line.decode().strip() + '\n'

tree = ET.fromstring(xml_data)

comments = tree.findall('comments/comment')

sum = 0

for comment in comments:
  count = int(comment.find('count').text)
  sum += count

print('XML =', sum)


# JSON 

import urllib.request, urllib.parse, urllib.error
import json

URL = 'http://py4e-data.dr-chuck.net/comments_1548414.json'

fhand = urllib.request.urlopen(URL)

json_data =''''''

for line in fhand:
  json_data += line.decode().strip() + '\n'

json_dict = json.loads(json_data)

comments = json_dict['comments']

sum = 0

for comment in comments:
  count = int(comment['count'])
  sum += count

print('JSON =', sum)