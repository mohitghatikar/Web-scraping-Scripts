# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:43:46 2016

@author: mohit
"""

"""
This script downloads the first 3 pages of articles (posts) written by Chris Ziegler.
Each page is stored in a separate html file.
"""

#import the two libraries we will be using in this script
import urllib2,os,sys,time

#make a new browser, this will download pages from the web for us. This is done by calling the 
#build_opener() method from the urllib2 library
browser=urllib2.build_opener()

#desguise the browser, so that websites think it is an actual browser running on a computer
#browser.addheaders=[('User-agent', 'Mozilla/5.0')]
browser.addheaders=[('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

#number of pages you want to retrieve
pagesToGet=3
author_name = 'chrisziegler'
#make a new folder to store the pages, but only if it doesn't already exist
if not os.path.exists('chrisziegler'):os.mkdir('chrisziegler')


"""
Note: The range() function
    the range(a,b) function returns the list of numbers from a all the way to (but excluding) b. 
    For example, range (1,4) will return  [1, 2, 3]
"""

#for every number in the range from 1 to pageNum+1  
for page in range(1,pagesToGet+1):
    
    print 'processing page :', page

    #prepare the link to the next page    
    url='http://www.theverge.com/users/'+str(author_name)+'/posts/'+str(page)

    #an exception might be thrown, so the code should be in a try-except block
    try:
        #use the browser to get the url. This is suspicious command that might blow up.
        response=browser.open(url)# this might throw an exception if something goes wrong.
    # response is equivalent to an enter key in chrome
    except Exception as e: # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()# get the exception information
        print 'ERROR FOR LINK:',url #print the link that cause the problem
        print error_type, 'Line:', error_info.tb_lineno #print error info and line that threw the exception
        continue#ignore this page. Abandon this and go back.
    
    #read the response in html format. This is essentially a long piece of text
    myHTML=response.read()

    #write the page to a new html file
    fwriter=open('chrisziegler/'+str(page)+'.html','w')
    fwriter.write(myHTML)
    fwriter.close()
    
    #wait for 2 seconds
    time.sleep(2)

# Get the first page, wait for 2 seconds. Then get second page and so on....
# This is because there might be a mismatch between chrome and python. Python is much faster. chrome is slow.
# the other is security. If someone makes more than 10 requests in 2 seconds. Then the request might be blocked.
# start with 5 seconds. And test it for 70 times. If it goes well, then decrease the number and so on.

