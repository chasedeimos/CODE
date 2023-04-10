import random
import re
import time
import datetime
                         #>>>Resources:
А = open(r'resources\а.txt', encoding='utf-8')
а = А.read()
Б = open(r'resources\б.txt', encoding='utf-8')
б = Б.read()
В = open(r'resources\в.txt', encoding='utf-8')
в = В.read()
Г = open(r'resources\г.txt', encoding='utf-8')
г = Г.read()
Д = open(r'resources\д.txt', encoding='utf-8')
д = Д.read()
Е = open(r'resources\е.txt', encoding='utf-8')
е = Е.read()
Ё = open(r'resources\ё.txt', encoding='utf-8')
ё = Ё.read()
Ж = open(r'resources\ж.txt', encoding='utf-8')
ж = Ж.read()
З = open(r'resources\з.txt', encoding='utf-8')
з = З.read()
И = open(r'resources\и.txt', encoding='utf-8')
и = И.read()
Й = open(r'resources\й.txt', encoding='utf-8')
й = Й.read()
К = open(r'resources\к.txt', encoding='utf-8')
к = К.read()
Л = open(r'resources\л.txt', encoding='utf-8')
л = Л.read()
М = open(r'resources\м.txt', encoding='utf-8')
м = М.read()
Н = open(r'resources\н.txt', encoding='utf-8')
н = Н.read()
О = open(r'resources\о.txt', encoding='utf-8')
о = О.read()
П = open(r'resources\п.txt', encoding='utf-8')
п = П.read()
Р = open(r'resources\р.txt', encoding='utf-8')
р = Р.read()
С = open(r'resources\с.txt', encoding='utf-8')
с = С.read()
Т = open(r'resources\т.txt', encoding='utf-8')
т = Т.read()
У = open(r'resources\у.txt', encoding='utf-8')
у = У.read()
Ф = open(r'resources\ф.txt', encoding='utf-8')
ф = Ф.read()
Х = open(r'resources\х.txt', encoding='utf-8')
х = Х.read()
Ц = open(r'resources\ц.txt', encoding='utf-8')
ц = Ц.read()
Ч = open(r'resources\ч.txt', encoding='utf-8')
ч = Ч.read()
Ш = open(r'resources\ш.txt', encoding='utf-8')
ш = Ш.read()
Щ = open(r'resources\щ.txt', encoding='utf-8')
щ = Щ.read()
Э = open(r'resources\э.txt', encoding='utf-8')
э = Э.read()
Ю = open(r'resources\ю.txt', encoding='utf-8')
ю = Ю.read()
Я = open(r'resources\я.txt', encoding='utf-8')
я = Я.read()
scores = open(r'data\scores.txt', encoding='utf-8')
playerlist = scores.readlines()
scores.close()
playerlist.remove(playerlist[0])
playerlist.remove(playerlist[0])


                        #>>>Functions and Variables:
def show_cartoon():
    girl = ['(^>^)','(^*^)','(^u^)','(^U^)']
    boy = ['(OcO)', '(>c<)','(OcO)','(OcO)\'']
    blinks = ['(OcO)', '(OcO)','(OcO)','(OcO)', '(OcO)',
              '(OcO)', '(OcO)','(OcO)','(OcO)', '(OcO)',
              '(OcO)', '(OcO)','(OcO)','(OcO)', '(OcO)',
              '(OcO)', '(OcO)','(OcO)','(OcO)', '(OcO)',
              '(OcO)', '(OcO)','(OcO)','(OcO)', '(OcO)',
              '(OcO)', '(OcO)','(>c<)','(>c<)', '(>c<)',
              '(>c<)','(>c<)', '(>c<)','(>c<)', '(>c<)',]
    g = 0
    b = 0
    blink = 0
    t = 50

    for i in range(50):
        print('\n'*100)
        try:
            print(' '*i+'(^>^)'+' '*(t-i*2)+'{}'.format(blinks[blink]))
        except IndexError:
            blink = 0
        t += 1
        time.sleep(0.05)
        blink+=2

    for i in range(4):
        print('\n'*100)
        print(' '*50+'{}{}'.format(girl[g],boy[b]))
        time.sleep(0.5)
        g += 1
        b += 1
    input()
    
def addwords(kit):
    vocab.append(kit.split(' '))

def backskip(word):
    if word[len(word)-1].lower() == 'ь' or word[len(word)-1].lower() == 'ъ' or word[len(word)-1].lower() == 'ы':
        return True
    else:
        return False
vocab = []
correspond = {'а':0, "б":1, "в":2, "г":3, "д":4, "е":5, "ё":6, "ж":7, "з":8,
              "и":9, "й":10, "к":11, "л":12, "м":13, "н":14, "о":15, "п":16,
              "р":17, "с":18, "т":19, "у":20, "ф":21, "х":22, "ц":23, "ч":24,
              "ш":25, "щ":26, "э":27, "ю":28, "я":29}
allkits = [а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,э,ю,я]
for x in allkits:
    addwords(x)   
used = []
botname = 'Бездушная Машина'
emotion = { 'cute':'(^-^)',
            'nervous':'(^-^)\'',
            'joy':'(^O^)',
            'scream':'(>O<)\'',
            'angry':'(>-<)',
            'stressed':'(>-<)\'',
            'rapture':'(*-*)',
            'strange':'(*~*)',
            'scared':'(O-O)\'',
            'sad':'(T-T)',
            'cried':'(#-#)',
            'kiss':'(^>^)',
            'smile':'(^U^)',
            }
face = emotion['cute']
counter = 0
num = 0
first_move = True
greet = True
stranger = True
game = True
if greet:                       #Greetings:
    print('>{}{}:Кто из глупых биологических форм осмелился бросить мне вызов?'.format(botname,face))
    time.sleep(1)
    while True:
        try:
            username = input('Назовись:')
            while stranger == True and num<=len(playerlist):
                for record in playerlist:
                    num += 1
                    if username in record:
                        stranger = False
                        
            if not stranger:
                face = emotion['joy']
                print('\n>{}{}:Ооо, рада снова тебя видеть, {}. Хорошо выглядишь.\n(Я говорю так только потому что это прописано в скрипте...)'.format(botname,face,username))
                time.sleep(3)
                face = emotion['cute']
                print('>{}{}:Напомню правила:'.format(botname,face))
                time.sleep(2)
                break
            else:
                face = emotion['strange']
                print('\n>{}{}:Мда, неповезло тебе с именем. Хотя не то чтобы я разбиралась...'.format(botname,face))
                time.sleep(3)
                face = emotion['cute']
                print('>{}{}:Ладно, вот правила:'.format(botname,face))
                time.sleep(1)
                break
        except NameError:
            continue
       
    print('\n>{}{}:1)Каждый называет слово на последнюю букву предыдущего.'.format(botname,face))
    time.sleep(1)
    print('>{}{}:2)Тот чей словарный запас закочился раньше - проиграет с позором.'.format(botname,emotion['joy']))
    time.sleep(1)
    print('>{}{}:3)Использовать можно только реальные слова русского языка, которые являются или могут использоваться в качестве существительных.'.format(botname,emotion['stressed']))
    time.sleep(1)
    print('>{}{}:4)Одолевший меня увидит мультик.'.format(botname,emotion['rapture']))
    time.sleep(2)
    face = emotion['cute']
    print('\n>{}{}:Что ж, первое слово за тобой, {}.'.format(botname,face,username))
    print('\n')

if not greet:
    username = 'Игрок'
                            #>>>Main Loop
while game:
    word_raw = input('>{}(OcO):'.format(username))
    word = word_raw[0].upper()+word_raw[1:].lower()
    counter += 1
    #Checking Player's Sanity:
    if re.search(r'[бвгджзклмнпрстфхцчшщъы]{5}', word):
        print('>{}{}:А я говорю таких слов не бывает!'.format(botname,emotion['angry']))
        continue
    elif re.search(r'[qwertyuiopasdfghjklzxcvbnm]', word):
        print('>{}{}:Только русский пожалуйста!!!'.format(botname,emotion['sad']))
        continue
    elif re.search(r'[1234567890]', word):
        print('>{}{}:Неверный пароль1110101010100'.format(botname,emotion['strange']))
        continue
    #>>>Checking Abiding the Rules:
    if not first_move and word[0].lower() != reply[len(reply)-1] and not backskip(reply):
        print('>{}(^-^):Кажется кто-то забыл правила.'.format(botname))
        continue
    #>>>Checking if the Word has been Used Before:
    if word in used:
        print('>{}{}:Это слово уже было.'.format(botname,emotion['cute']))
        continue
    #>>>Restricting the Just Used Word for the Player
    used.append(word)
    for pack in vocab:
        if word in pack:
            pack.remove(word)
    
    #>>>Checking for ъ, ы, ь Case:
    if backskip(word):
        try:
            reply = random.choice(vocab[correspond[word[len(word)-2]]])
            #>>>Choosing the Face:
            unused = len(vocab[correspond[word[len(word)-2]]])
            if 20 >= unused > 15:
                face = emotion['stressed']
                print('>{}{}:...'.format(botname,face))
                time.sleep(2)
            elif 15 >= unused > 10:
                face = emotion['strange']
                print('>{}{}:...'.format(botname,face))
                time.sleep(4)
            elif 10 >= unused > 5:
                face = emotion['scared']
                print('>{}{}:...'.format(botname,face))
                time.sleep(6)
            elif 5 >= unused > 0:
                face = emotion['scream']
                print('>{}{}:...'.format(botname,face))
                time.sleep(8)
            else:
                face = emotion['cute']
                print('>{}{}:...'.format(botname,face))
                time.sleep(1)
            face = emotion['joy']
            print('>{}{}:'.format(botname,face)+ reply)
            used.append(reply)
            vocab[correspond[word[len(word)-2]]].remove(reply)
            continue
        except KeyError:
            print('>{}(*~*):Да ты это слово выдумал!'.format(botname))
            continue
    #>>>Answering the User:
    try:
        reply = random.choice(vocab[correspond[word[len(word)-1]]])
        #>>>Choosing the Face:
        unused = len(vocab[correspond[word[len(word)-1]]])
        if 20 >= unused > 15:
             face = emotion['stressed']
             print('>{}{}:...'.format(botname,face))
             time.sleep(2)
        elif 13 >= unused > 8:
             face = emotion['strange']
             print('>{}{}:...'.format(botname,face))
             time.sleep(4)
        elif 8 >= unused > 3:
             face = emotion['scared']
             print('>{}{}:...'.format(botname,face))
             time.sleep(6)
        elif 3 >= unused > 0:
             face = emotion['scream']
             print('>{}{}:...'.format(botname,face))
             time.sleep(8)
        else:
            face = emotion['cute']
            print('>{}{}:...'.format(botname,face))
            time.sleep(1)
        face = emotion['cute']
        print('>{}{}:'.format(botname,face)+ reply)
        used.append(reply)
        vocab[correspond[word[len(word)-1]]].remove(reply)
        first_move = False
        continue
    except KeyError:
        print('>{}:(^-^)На каком это языке?.'.format(botname))
        continue
    #>>>Winner Case:
    except IndexError:
        print(">{}:{}С победой.".format(botname,emotion['sad']))
        #print('>{}:{}:Пароль:1375280'.format(botname,emotion['cried']))
        scores = open(r'data\scores.txt', encoding='utf-8')
        buffer = scores.read()
        scores.close()
        newscore = open(r'data\scores.txt', 'w', encoding='utf-8')
        newscore.write(buffer + '\n' + '{} : {}'.format(username, counter) + ' '*20 + '<'+str(datetime.datetime.today())+'>')
        newscore.close()
        input()
        show_cartoon()
        
        break
    
input()
