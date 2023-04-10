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

def addwords(kit):
    vocab.append(kit.split(' '))

vocab = []
correspond = {'а':0, "б":1, "в":2, "г":3, "д":4, "е":5, "ё":6, "ж":7, "з":8,
              "и":9, "й":10, "к":11, "л":12, "м":13, "н":14, "о":15, "п":16,
              "р":17, "с":18, "т":19, "у":20, "ф":21, "х":22, "ц":23, "ч":24,
              "ш":25, "щ":26, "э":27, "ю":28, "я":29}
allkits = [а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,э,ю,я]
for x in allkits:
    addwords(x)

Reading = True
while Reading:
    letter = input('Letter:')
    for word in vocab[correspond[letter]]:
        print(word + ' '*50 + str(len(vocab[correspond[letter]])))
        vocab[correspond[letter]].remove(word)
        next = input()
        if next == 'exit':
            Reading = False
            break
        if next == 'newletter':
            break
