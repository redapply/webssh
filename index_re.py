#!/usr/bin/python3
print('Content-type: text/html; charset=UTF-8\n')
import cgi, os

dirfiles = os.listdir('data')
listStr=''
for item in dirfiles:
  listStr=listStr+'<li><a href="index_re.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form['id'].value
  desc = open('data/'+pageId,'r').read()
else:
  pageId='Welcome to Web Python'
  desc = 'Hello, Python Web'


print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index_re.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href='create_re.py'>Create</a>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId,desc=desc,listStr=listStr))