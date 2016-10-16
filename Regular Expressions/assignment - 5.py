# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 00:22:07 2016

@author: Mohit Ravi Ghatikar

CWID: 10405877

HW5: Sentence Splitter

BIA 660A
"""

import re

fr=open('C:\Users\mohit\Desktop\Spring BIA\Web Analytics\python scripts\week 6\input.txt')
text=fr.read().strip()
fr.close()

Sentence_no = 0  
sentence = re.finditer('.+?\. |.+[^,:/#_]+?\.',text)
# The above regual expression works well expect for the last line
for M in sentence:
    link = M.group()
    if link.count('.')==2:# Overfitting. Split the last sentence if number of dots is equal to 2
        Last_sentence = re.finditer('.+?\.',link)
        Overfitting_sentence_no=7
        for Last in Last_sentence:
            print Overfitting_sentence_no,'-',Last.group()
            Overfitting_sentence_no+=1
    else:
        Sentence_no+=1
        print Sentence_no,'-',link
        


        