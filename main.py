#!/usr/bin/env python
import cgi, cgitb

form1 = cgi.FieldStorage()
name = form1.getvalue("name")
print('Content-type:text/html \n\n')
print("Hello Web Development" + name)
