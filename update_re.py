#!/usr/bin/python3
import os
import cgi
print('Content-type: text/html; charset=UTF-8\n')

dirfiles = os.listdir('data')
listStr = ''
for item in dirfiles:
  listStr = listStr + \
      '<li><a href="index_re.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form['id'].value
  desc = open('data/'+pageId, 'r').read()
else:
  pageId = 'Welcome to Web Python'
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
  <form action='process_update_re.py' method='post'>
        <input type='hidden' name = 'pageId' value='{form_title}'>
        <p><input type = "text" name="title" placeholder="title" value='{form_title}'></p>
        <p><textarea rows="4" name="description" placeholder='description'>{form_desc}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId,listStr=listStr,form_title=pageId,form_desc=desc))
