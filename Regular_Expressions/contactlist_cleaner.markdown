# description contact_scrapper.py

## Regular expressions are made for processing text.
---
### Documentation:

[Regular Expressions](https://docs.python.org/3/library/re.html)  
[open()](https://docs.python.org/3/library/functions.html#open)  
[file_object.close()](https://docs.python.org/3/library/io.html#io.IOBase.close)  
[file_object.read()](https://docs.python.org/3/library/io.html#io.RawIOBase.read)  

---
### New Terms:
re.match(pattern, text, flags) - Tries to match a pattern against the beginning of the text.  

re.search(pattern, text, flags) - Tries to match a pattern anywhere in the text. Returns the first match.  

---
#### Escape Characters
\w - matches any Unicode word Character.  
\W - matches anthing that isn't a Unicode character.  
\s - any whitespace.  
\S - anything that isn't whitespace.  
\d - any number 0 to 9  
\D - any non-number  
\b - matches word boundaries  
\B - anything that isn't the edges of a word.  

---
#### Counts
\w{3} - matches any three word characters in a row.  
\w{,3} - matches 0, 1, 2, or 3 word characters in a row.  
\w{3,} - matches 3 or more word characters in a row. There's no upper limit.  
\w{3, 5} - matches 3, 4, or 5 word characters in a row.  
\w? - matches 0 or 1 word characters.  
\w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.  
\w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.  
.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.  

---
#### Sets

[abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.  
[a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.  
[0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.  

---
#### Negation

[^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.  
re.IGNORECASE or re.I - flag to make a search case-insensitive.   re.match('A', 'apple', re.I) would find the 'a' in 'apple'.  
re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.  

---
#### Groups
([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)  
(?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').  
.groups() - method to show all of the groups on a Match object.  
re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.  
^ - specifies, in a pattern, the beginning of the string.  
$ - specifies, in a pattern, the end of the string.  

---
#### Compiling and Loops

re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.  
.groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.  
re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.  
.group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.  



---
#### examples

Notes:
#### A better way to read files

'''python
with open("some_file.txt") as open_file:
    data = open_file.read()
'''

---
__Word-length__

Create a function named find_words that takes a count and finds a string with
that many characters.

'''python
import re

def find_words(cnt,s):
    return re.findall(r'\w{{{:d},}}'.format(cnt), s)
'''
or
'''python
def find_words():
    return re.findall(r'\w{' + str(count) + ',}', string)
'''

---
__Players - Dictionary__  
Create a variable named players that is a re.search() or re.match() to capture three groups: last_name, first_name, and score. It should include re.MULTILINE. THEN. Create a class named Player that has those same three attributes, last_name, first_name, and score. You should be able to set them through __init__.

'''python
import re
string = '''Bot, Doc: 21
Blender, Andrew: 27
McHeat, Dave: 10
Rain, Joy: 22
Cricket, Don: 18'''

players = re.search(r'''
    (?P<last_name>[\w]*)
    ,\s
    (?P<first_name>[\w ]*)
    :\s
    (?P<score>[\d]*)
''', string, re.X|re.M)

class Player:
  last_name = ""
  first_name = ""
  score = ""

  def __init__(self, last_name=last_name, first_name=first_name, score=score):
    self.last_name = last_name
    self.first_name = first_name
    self.score = score

'''
---
