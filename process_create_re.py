#!/usr/bin/python3
import os
import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

opened_file = open('data/'+title,'w')
opened_file.write(description)
opened_file.close()

print('Location: index_re.py?id='+title)
print()

