#!/usr/bin/python3


import cgi
form = cgi.FieldStorage()
title = form['title'].value
descrtion = form['description'].value

files = open('data/'+title,'w') 
files.write(descrtion)

print('Location: index.py?id='+title)
print()
