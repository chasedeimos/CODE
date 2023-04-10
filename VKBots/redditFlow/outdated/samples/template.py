from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
import pytesseract
from PIL import Image
from googletrans import Translator
import time
tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Pretend to be a human with human headers to gain access
hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Receive reddit page contents
pmolol = 'https://www.reddit.com/r/memes/new'
request = Request(pmolol, headers=hdrs)
response = urlopen(request)
soup = BeautifulSoup(response,'lxml')

# Execute all the scripts on the paged
'''
options = webdriver.FirefoxOptions()
options.set_headless()
browser = webdriver.Firefox(firefox_options = options)

scripts = soup.find_all('script')
for script in scripts:
    try:
        browser.execute_script(script.text)
    except:
        pass
'''
# Identify all pictures on the page
pics = [
        img for img in soup.find_all('img')
        if 'renderTimingPixel' not in img['src']
        and 'www.redditstatic.com' not in img['src']
        ]

# Download all pics and map their paths to their translated texts
def translate(text):
    t = Translator()
    translated = t.translate(text, src='en', dest='ru')
    return translated.text

mapp = {}
for pic in pics:
    src = pic['src']
    path = r'C:\Users\rgstr\Desktop\{}.jpg'.format(src[-5:-1])
    urlretrieve(src,path)
    time.sleep(3)
    text = pytesseract.image_to_string(Image.open(path))
    mapp[path] = text
    
for pic in mapp:
    print(mapp[pic])
    print("Translation:")
    print(translate(mapp[pic]))
    print("-----------------------")
    
