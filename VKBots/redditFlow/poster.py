from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError
import time
import requests

import scanner

# Set up a proxy
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

# Set headers
reddit = 'https://www.reddit.com/r/memes/'
headers = {
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
        }

#scanner.Scan(reddit,headers)



