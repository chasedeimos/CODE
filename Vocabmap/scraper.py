from urllib.request import Request, urlopen
from urllib.parse import quote   
from bs4 import BeautifulSoup as bs
import io
import re

headers = {
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
       }

def findExamples(word):
    # Retrieve the examples 
    url = 'https://www.purpleculture.net/dictionary-details/?word=' + quote(word)
    request = Request(url, headers=headers)
    response = urlopen(request)
    soup = bs(response, 'html.parser')
    exampleElements = soup.findAll('span', {'class': 'samplesen'})
    meaningElements = soup.findAll('div', {'class':'sample_en'})
    examples = []
    meanings = []
    for i in range(0, len(exampleElements) - 1):
        example = re.sub("[a-zāáǎàōóǒòēéěèīíìǐūúǔùǖǘǚǜü ]", '', exampleElements[i].text)
        meaning = meaningElements[i].text
        print(meaning, len(meaning))
        if len(meaning) <= 75:
            examples.append(example)
            meanings.append(meaning)
    examples.append('')
    meanings.append('')
    structure = [examples, meanings]
    return structure

if __name__ == '__main__':
    structure = findExamples('必')
