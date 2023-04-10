from urllib.request import *
from bs4 import BeautifulSoup
from vk_api import VkApi

def Scan():
    # Seeing what's been scanned already
    file = open('stories.txt','r',encoding='utf-8')
    allStories = file.read()
    file.close()
    # Setting up proxy
    proxy = ProxyHandler({'https':'54.37.154.101'})
    opener = build_opener(proxy)
    install_opener(opener)
    # Retreiving the site
    site = 'http://chinesereadingpractice.com/page/3'
    headers = {
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Connection': 'keep-alive',
       'Referer':'http://www.google.com/'}
    request = Request(site,headers=headers)
    html = urlopen(request).read()
    soup = BeautifulSoup(html,'lxml')
    titles = []
    stories = []
    lvls = []
    h2s = soup.findAll('h2',{'class':'entry-title heading-size-1'})
    # Do for each story
    for h2 in h2s:
        # Find the difficulty level
        div = h2.find_parent('div')
        level = div.find('div',{'class':'entry-categories-inner'}).find('a').text
        if level == 'Beginner':
            lvl = 'HSK 1-2'
        elif level == 'Intermediate':
            lvl = 'HSK 3-4'
        elif level == 'Advanced':
            lvl = 'HSK 5-6'
        else:
            continue
        lvls.append(lvl)
        # Follow the link to the story page
        link = h2.find('a')['href']
        request = Request(link,headers=headers)
        html = urlopen(request).read()
        soup = BeautifulSoup(html,'lxml')
        textbox = soup.find('div',{'id':'chinesetext'})
        # Collecting stories
        ps = textbox.findAll('p',{'class':None})
        story = []
        for p in ps:
            if p.find('a') == None:
                story.append(p.text)
        story = '\n'.join(story)
        if story not in allStories:
            stories.append(story)
        else:
            continue
        # Collecting titles
        try:
            title = textbox.find('h4').text
        except AttributeError:
            title = None
        finally:
            titles.append(title)
            print('{}\n'.format(lvl))
            print(title)
            print(story)
            print('\n')
    # Create an array structure with all the stories merged with their titles and levels
    struct = []
    for i in range(0,len(stories)):
        lvl = lvls[i]
        title = titles[i]
        story = stories[i]
        if titles[i] is not None:
            struct.append('{}\n\n'.format(lvl) + title + '\n' + story)
        else:
            struct.append('{}\n\n'.format(lvl) + story)
    # Adding new stories to the 'stories' textfile
    file = open('stories.txt','w',encoding='utf-8')
    for story in struct:
        file.write(story)
        file.write('\n')
    file.close()
    
    storynum = len(struct)
    print('> {} new stories were found.'.format(storynum))
    return struct

def Post(struct):
    # Seeing what's been posted already
    file = open('posts.txt','r',encoding='utf-8')
    allPosts = file.read()
    file.close()
    # Logging in
    session = VkApi('+77479170861','1DER26eed@netrunnerghost')
    session.auth()
    vk = session.get_api()
    owner_id = '-196417294'
    # Posting the stories
    for post in struct:
        if post not in allPosts:
            vk.wall.post(owner_id=owner_id, from_group=1, message = post)
        # Adding posted stories to the 'posts' textfile
        file = open('posts.txt','w',encoding='utf-8')
        for story in struct:
                file.write(story)
                file.write('\n')
        file.close()

if __name__ == '__main__':
    struct = Scan()
    # If there's something to upload, upload it
    if len(struct) != 0:
        Post(struct)
        print('> posted successfully.')
    input()
