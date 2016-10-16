"""
A set of examples for the re package
"""

import re



print '-------Example 1-------------'
 
text='The sky is blue!'
#Example 1 
#search looks for a substring inside the given string. If no match is found, it returns None. 
#If a match is found, it returns a match object. 
M=re.search('sky',text)
print M
print M.start(),M.end() # print the starting point (inclusive) and ending point (exclusive) of the substring in the given string
    
M=re.search('house',text)
print M

print '-------Example 2-------------'

#Example 2
#If there are multiple matches, only the first one is considered
text='The sky is blue! The house is white!'
M=re.search('is',text)
print M.start(),M.end()

print '-------Example 3--------------'

#Example 3
#What if we want to get all the matches of a substring?
text='The sky is blue! The house is white!'
Ms=re.finditer('is',text)
for M in Ms:
    print M.start(),M.end()

print '-------Example 4-=------------'

#Example 4:
#In many cases, we want to find partial matches. 
#We can use .+? to represent "1 or more characters until you find the termination sequence."
#What is the termination sequence? It's whatever follows .+?
text='The sky is blue!'
M=re.search('The .+? is .+?!',text)
print M.start(),M.end()


print '-------Example 5--------------'

#what if I want to focus on a specific part of the match?
text='The sky is blue!'
M=re.search('The (.+?) is (.+?)!',text)
print M.group(1),M.group(2)



print '-------Example 6--------------'

#Example 6 
#What about multiple approximate matches?
text='The sky is blue! The house is white! The ball is red!'
Ms=re.finditer('The (.+?) is (.+?)!',text)
for M in Ms:
    print M.group(1), M.group(2)





