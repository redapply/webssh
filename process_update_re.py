#!/usr/bin/python3
import cgi
import os
form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
description = form['description'].value

files = open('data/'+pageId, 'w')
files.write(description)
files.close()
os.rename('data/'+pageId, 'data/'+title)

#Redirection
print('Location: index_re.py?id='+title)
print()
