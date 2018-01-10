#!/usr/bin/env python

""" Using Regular Expressions, lets clear up a text file."""

__author__ = "Johnny Romano"
__date__ = "2019-01-08"

import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

last_name = r'Romano'
first_name = r'Johnny'

# using match for beginning of string.
#print(re.match(last_name, data))

# using search for any part of string.
#print(re.search(first_name, data))

#print(re.search(r'\d\d\d-\d\d\d\d, data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-d{4}', data))

#print(re.findall(r'\w+, \w+', data))

# match email pattern
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

# match word in set of 9 word boundary
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))

#print(re.findall(r'''
#    \b@[-\w\d.]* # First a word boundary, an @, and then any number of Characters
#    [^gov\t]+ # Ignore 1+ instances of the letters 'g', 'o',  or 'v' and a tab.
#    \b # Match another word boundary
#''', data, re.VERBOSE|re.I))


#print(re.findall(r"""
#    \b[-\w]*, # find a word boundary, 1+ hyphens or characters, and a coma
#    \s # Find 1 whitespace
#    [-\w ]+ # 1+ hypens and characters and explicit spaces
#    [^\t\n] # Ignore tabs and newlines
#""", data, re.X))

# Use a string like a dictionary
#line = re.search(r'''
#    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and First names
#    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
#    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
#    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and Company
#    (?P<twitter>@[\w\d]+)?$  # Twitter
#''', data, re.X|re.MULTILINE)

#print(line)
#print(line.groupdict())

# Use a string like a dictionary
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and First names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and Company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.M)

#print(re.search(line, data).groupdict())
# same as
#print(line.search(data).groupdict())

# Search Data for 'name'
#for match in line.finditer(data):
#    print(match.group('name'))

#print(line)
# Search Data for 'first name + Last name + <email>'
for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
