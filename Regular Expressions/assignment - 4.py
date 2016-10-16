"""
HW-4 : Verified Purchase

Author: Mohit Ravi Ghatikar

CWID: 10405877

"""

import re

fconn=open('reviews.html')
html=fconn.read()#read the entire html into this variable
fconn.close()

#find all the matches of the given expression which has verified purchases in them
matches_with_verified=re.finditer('<div id="R.*?" class="a-section review".*?\
<span class="a-icon-alt">(.*?) out of 5 stars</span>.*?\
<a class="a-size-base a-link-normal review-title a-color-base a-text-bold" href="/gp/.*?>(.*?)</a>.*?\
<a class="a-size-base a-link-normal author" href="/gp/.*?>(.*?)</a>.*?\
<span class="a-size-base a-color-secondary review-date">on (.*?)</span>.*?\
<span class="a-size-mini a-color-state a-text-bold">(Verified Purchase)</span>.*?\
<span class="a-size-base review-text">(.*?)</span>.*?',html)

#find all the matches of the given expression which does not have verified purchases in them
matches_without_verified=re.finditer('<div id="R.*?" class="a-section review".*?\
<span class="a-icon-alt">(.*?) out of 5 stars</span>.*?\
<a class="a-size-base a-link-normal review-title a-color-base a-text-bold" href="/gp/.*?>(.*?)</a>.*?\
<a class="a-size-base a-link-normal author" href="/gp/.*?>(.*?)</a>.*?\
<span class="a-size-base a-color-secondary review-date">on (.*?)</span>.*?\
</i>Style Name: U.S. Version</a></div>.*?\
<span class="a-size-base review-text">(.*?)</span>.*?',html)

# Print the output for verified purchases
for M in matches_with_verified:
    stars=M.group(1)
    title=M.group(2)
    user=M.group(3)
    date = M.group(4)
    Verified = M.group(5)
    text = M.group(6)
    

    print stars,title,user,date,Verified,text
    
# print the output without verified purchases
for M in matches_without_verified:
    stars=M.group(1)
    title=M.group(2)
    user=M.group(3)
    date = M.group(4)
    text = M.group(5)
    
    print stars,title,user,date,text