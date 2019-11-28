from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time  
   
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

browser = webdriver.Chrome()  
browser.get('https://www.youtube.com/') 

time.sleep(2)  

search = browser.find_elements_by_xpath('//*[@id="search"]')

query = input('Enter the song and artist name separated by space\n')
time.sleep(10)

s = ''
lis = query.split()
for i in range(len(lis)):
    if i!= len(lis)-1:
        s = s + (lis[i]) + '+'
    else:
        s = s + lis[i]

search[0].send_keys(query)
search[0].send_keys(Keys.ENTER)

my_url = 'https://www.youtube.com/results?search_query='+s

uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html, 'html.parser')

container = page_soup.find_all('div',{"class":"yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix"})

contain = container[0].find_all('a')

link = 'https://www.youtube.com'+(contain[0]['href'])

browser.get('https://mp3-youtube.download/en')
time.sleep(2)

search = browser.find_element_by_xpath('//*[@id="app"]/div/article/div/div/input')
search.send_keys(link)
search.send_keys(Keys.ENTER)

time.sleep(5)

tabs = browser.window_handles
browser.switch_to.window(tabs[1])
browser.close();
browser.switch_to.window(tabs[0])

time.sleep(10)

download = browser.find_element_by_xpath('//*[@id="app"]/div/article/div/p[2]/a')
download.click()
