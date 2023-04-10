userpass = input("Enter a Possible WiFi Password\n:")
sym = set()
numlist = ["0","1","2","3","4","5","6","7","8","9"]
for i in range(10):
    sym.add(numlist[i])
letlist = "qwertyuiopasdfghjklzxcvbnm"
for i in range(len(letlist)):
    sym.add(letlist[i])
    sym.add(letlist[i].upper())
password = ["0","0","0","0","0","0","0","0"]



def sub(i):
   if i>=0:
    for c in sym:
        comppass = "".join(password)
        print("Now Trying:"+comppass)
        if comppass == userpass:
            print("Your Password " + comppass + " Has Been Cracked.")
        password[i] = c
        sub(i-1)
        sub(i-2)
        sub(i-3)
        sub(i-4)
        sub(i-5)
        sub(i-6)
        sub(i-7)
    


sub(7)

input()
  

