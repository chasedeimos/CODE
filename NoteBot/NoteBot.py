import pygame
import random
import time
from pygame.mixer import *
pygame.mixer.init()

#Locating Notes:
C = r'notes\C.mp3'
#Cd = r'notes\Cd.mp3'
D = r'notes\D.mp3'
#Dd = r'notes\Dd.mp3'
E = r'notes\E.mp3'
F = r'notes\F.mp3'
#Fd = r'notes\Fd.mp3'
G = r'notes\G.mp3'
#Gd = r'notes\Gd.mp3'
A = r'notes\A.mp3'
#Ad = r'notes\Ad.mp3'
B = r'notes\B.mp3'
c = r'notes\c1.mp3'
#cd = r'notes\cd1.mp3'
d = r'notes\d1.mp3'
#dd = r'notes\dd1.mp3'
e = r'notes\e1.mp3'
f = r'notes\f1.mp3'
#fd = r'notes\fd1.mp3'
g = r'notes\g1.mp3'
#gd = r'notes\gd1.mp3'
a = r'notes\a1.mp3'
#ad = r'notes\ad1.mp3'
b = r'notes\b1.mp3'
c = r'notes\c1.mp3'

#Defining Chords:
Cc = [C, E, G]
Dc = [D, F, A]
Ec = [E, G, B]
Fc = [F, A, C]
Gc = [G, B, D]
Ac = [A, C, E]
Bc = [A, C, F]
chords = [Cc, Dc, Ec, Fc, Gc, Ac, Bc]
pianoroll = [C, D, E, F, G, A, B, c, d, e, f, g, a, b, c]
wait = [0.5,1]
intervals = [4]
while True:
    rep = random.choice(intervals)
    chord = random.choice(chords)
    print(chord)
    while rep>0:
        for note in chord:
            music.load(note)
            print(note)
            music.play()
            time.sleep(random.choice(wait))
        note = pianoroll[random.randint(0,(len(pianoroll)-1))]
        music.load(note)
        print(note)
        music.play()
        time.sleep(random.choice(wait))

        rep -= 1
            
    

            
        
    '''   
    music.load(pianoroll[random.randint(0,(len(pianoroll)-1))])
    music.play()
    time.sleep(random.choice(wait))
    '''
input()
