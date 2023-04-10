import random
num = random.randint(1,9)
tries = 0
lim = 5
used = []

while tries < lim:
    print("I'm thinking about a number between 0 and 10")
    
    if tries > 0:
        print("and it's not " + str(used) + "\n")

        
    ans = int(input("What's your guess:"))

    if len(str(ans)) > 1 or ans == 0:
        print("\nEnter a number between 0 and 10\nExcluding 0 and 10\n")
        continue

    
    if ans in used:
        print("\nYou named it before\n")
        continue

    tries += 1
    
    
    
    if ans == num:
        print("\nYou're God Damn Right!")
        if tries == 1:
            word = "try"
        else:
            word = "tries"
        print("Number {0} Guessed in {1} {2}.".format(num,tries,word))
        break
    else:
        print("\nYou're Wrong")
        left = lim - tries
        if left == 1:
            word = "try"
        else:
            word = "tries"
        print("You have {0} {1} left.\n".format(left,word))
        used.append(ans)
        continue
    
#this input is to close the program
input()
