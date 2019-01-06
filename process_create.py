#!/usr/bin/python3
print('Content-type: text/html; charset=UTF-8\n')

import cgi
form = cgi.FieldStorage()
title = form['title'].value
descrtion = form['description'].value

print(title, descrtion)

