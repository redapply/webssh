#!/usr/bin/python3
print('Content-type: text/html; charset=UTF-8\n')
import cgi, os

def get_list():

    files = os.listdir('data')
    listStr=''
    for item in files:
        listStr= listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
    
form = cgi.FieldStorage()
if 'id' in form :
    pageId = form['id'].value
    description = open('data/'+pageId,'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, Web'

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB1</a></h1>
  <ol>
    {listStr}
  </ol>
 
  <a href="create.py">create</a>
  <form action='process_update.py' method='post'>
    <input type='hidden' name = 'pageId' value="{form_default_tilte}">
    <p><input type="text" name='title' placeholder='title' value="{form_default_tilte}"></p>
    <p><textarea rows="4" name='description' placeholder='description'>{form_default_description}</textarea>
    <p><input type='submit'></p>
    </form>
 </body>
</html>
'''.format(title=pageId,desc=description,listStr=get_list(),form_default_tilte=pageId,form_default_description=description))