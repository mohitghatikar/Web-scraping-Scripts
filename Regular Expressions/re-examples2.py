import re

fr=open('input.txt')
text=fr.read().strip()
fr.close()


print '-------------------------1--------------------------'
#print the number of times that 'insulin' appears in the document
print 'Insulin Count:', len(re.findall('insulin',text, re.I))


print '------------------------2---------------------------'
#find all occurences of  the word 'insulin' followed by a word starting with a letter 's'. Print the 's'-word for each occurence    
matches=re.finditer('insulin[^\w]+(s[\w\d]+)',text)
for M in matches:
    print M.group(1)

print '------------------------3---------------------------'
#print all the links in the input
links=re.findall('http.+?[^\w\d:/\.\-#]',text)
for link in links:
    print link.strip()[:-1]
    

print '-----------------------4----------------------------'    
#print the domain of each link in the input
links=re.findall('http.?//.+?[^\w\d:\.\-#]',text)
for link in links:
    print link.strip()[:-1]

   

print '-----------------------5----------------------------'    
#replace all non-letter and non-digit characters with a space
clean=re.sub('\W',' ',text)
print clean


print '-----------------------6----------------------------'    
#replace all white-space sequences in clean with  a single space
cleaner=re.sub(' +',' ',clean)
print cleaner


print '-----------------------7----------------------------'    
#print all phrases that start with the name of the drug and end at the end of the sentence.
matches=re.finditer('metformin.*?\.[A-Z\n ]',text,re.I)
for M in matches:
    print M.group(0).strip()

    
print '-----------------------8----------------------------'    
#replace the word 'metformin' with the word 'aspirin' (case insensitive)
print re.sub('[mM]etformin','Aspirin',text)

    
    
print '-----------------------9----------------------------'    
#print the last and first word of the file
first=re.search('\w+',text).group(0)
print first
last=re.search('[\w\.]+\Z',text).group(0)
if last[-1]=='.':print last[:-1]
else: print last


    
print '-----------------------10----------------------------'    
#remove all parenthesized phrases
newtext=re.sub('\(.*?\)','',text )
print newtext
