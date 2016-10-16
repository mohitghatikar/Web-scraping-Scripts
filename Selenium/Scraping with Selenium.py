# Author : Mohit Ravi Ghatikar
# CWID   : 10405877
# BIA 660 A
# Scraping with Selenium
# The objective is to download all the job listings for the keyword "Tableau" in the website Indeed.com

from selenium import webdriver
from bs4 import BeautifulSoup
import os,time,sys

#make a new folder to store the pages, but only if it doesn't already exist
if not os.path.exists('pages'):os.mkdir('pages')

# The URL for Indeed with the keyword - Tableau and location - New york
url = "http://www.indeed.com/jobs?q=tableau&l=new+york"

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

#sleep for 4 seconds
time.sleep(4)

# Click the button for Internships
button=driver.find_element_by_css_selector('#JOB_TYPE_rbo > ul > li:nth-child(4) > a')
button.click() #click on the button
time.sleep(3) #sleep

page=1
soup = BeautifulSoup(driver.page_source)
print 'page 1: done'
#write the page to a new html file
fwriter=open('pages/'+str(page)+'.html','w')
fwriter.write(str(soup))
fwriter.close()

page=2
while True: # Go on forever.
    cssPath='#resultsCol > div.pagination > a:nth-child(3) > span > span'
     
    try:
        button=driver.find_element_by_css_selector(cssPath)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break

    #click the button to go the next page, then sleep    
    button.click()
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source)
    print 'page',page,'done'
    #write the page to a new html file
    fwriter=open('pages/'+str(page)+'.html','w')
    fwriter.write(str(soup))
    fwriter.close()
    page+=1









