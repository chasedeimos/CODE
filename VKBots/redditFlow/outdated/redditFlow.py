from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request 
import time
import os

# Set up the Firefox driver
options = webdriver.FirefoxOptions()
options.set_headless()
driver = webdriver.Firefox(firefox_options=options)
# For Testing
print('Driver set!')

# Enter the page and wait until the "Join" button is loaded
driver.get('https://www.reddit.com/r/memes/')
# For Testing
print('Accessed the page!')
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Join']")))
finally:
    time.sleep(3)
    # For Testing
    print('Waiting Done!')

# Retrieve the loaded html and pass it to the soup
html = driver.find_element_by_xpath("//body").get_attribute('outerHTML')
soup = BeautifulSoup(html,'lxml')

# Get all pictures on the page and filter out irrelevant content
def URLFilter(elements):
    urls = [
            img['src']
            for img in elements
            if not img['src'].startswith('https://www.redditstatic.com/')
            and not img['src'].startswith('https://styles.redditmedia.com/')
            and not img['src'].startswith('https://preview.redd.it/award_images/')
            and not img['src'].startswith('https://c.aaxads.com/')
            and not img['src'].startswith('https://www.aaxdetect.com/')
            and not img['src'].startswith('https://b.thumbs.redditmedia.com/')
            ]
    return urls

urls = URLFilter(soup.findAll('img'))

# Filter out the promoted images
def noAds(urls):
    ads = soup.findAll('span', text='promoted')
    for ad in ads:
        div = ad.find_parent('div').find_parent('div').find_parent('div').find_parent('div')
        srcs = URLFilter(div.findAll('img'))
        for src in srcs:
            urls.remove(src)
    return urls

urls = noAds(urls)

# Store the urls that are already downloaded in a list
path = r"D:\Codes\!Projects\redditFlow\\"
folder = 'memes\\'
file = open(path+'urls.txt','r')
memory = []
for line in file.readlines():
    memory.append(line)
file.close()

# Set up a proxy
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
print('Proxy running')

# Download the images
for url in urls:
    if url not in memory:
        urllib.request.urlretrieve(url,path+folder+url[-5:-1]+'.jpg')
        request = urllib.request.urlopen(url)
        memory.append(url)
        # Make sure to sleep
        time.sleep(3)

# Write all the downloaded image urls into the text file
file = open(path+'urls.txt','w')
for url in memory:
    file.write(url+'\n')
file.close()


# For testing
print('Program Complete.')
