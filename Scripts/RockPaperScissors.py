import random

r = "Rock"
p = "Paper"
s = "Scissors"
su = 0
sc = 0
score = "                                      You | Computer\n                                  {}:{}".format(su,sc)

def compare(x,y):
 vs = str(x + " " + y)
 if r in vs:
    if p in vs:
        return p
    elif s in vs:
        return r
 else:
    return s

while True:
 try:
     x = int(input("Untill How Many Wins?\n:"))
 except TypeError:
     print("Please, Input a Number.")
     continue
 print("                                        GAME UNTILL " + str(x) + " WINS STARTS")
 
 while True:
  u1 = input(":")
  u = str(u1[0].upper() + u1[1:].lower())
  c = random.choice(["Rock","Paper","Scissors"])
 
 
  if u in [r,p,s]:
    print("                 You:"+u+"   |   Computer:"+c)
 
 
  res = compare(u,c) 
  if u==c:
    print("\n                           Draw!\n                     Friendship Wins!")
  elif res == u:
    print("\n                         You Win!")
    su += 1
  elif res == c:
    print("\n                     Computer Wins!")
    sc += 1
  else:
    print("                     Incorrect Input.")
  score = "                                                     You | Computer\n                                                        {}:{}".format(su,sc)   
  print(score)
  if su==x:
     print("\nCongratulations, You Won The Match!")
     break
  if sc==x:
     print("\nYou Lose The Match.")
     break

 
 


 rep = input("\nWant To Play Again?\n:")
 yep = ["y","Y","Yes","yes","Yep","yep","Yeah","yeah","Yea","yea","Da","da","U-huh","u-huh","Sure","sure","Of course","of course"]
 if rep in yep:
     su=0
     sc=0
     continue
 else:
     break


