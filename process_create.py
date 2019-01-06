#!/usr/bin/python3


import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

files = open('data/'+title,'w') 
files.write(description)

#Redirection
print('Location: index.py?id='+title)
print()
