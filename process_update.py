#!/usr/bin/python3


import cgi,os
form = cgi.FieldStorage()
pageId= form['pageId'].value
title = form['title'].value
description = form['description'].value

files = open('data/'+pageId,'w') 
files.write(description)

os.rename(pageId,title)

files.close()


#Redirection
print('Location: index.py?id='+title)
print()
