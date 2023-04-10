import time
import numberMaker
import numberGuesser
num = numberMaker.num
print("{0} has a number in her head".format(numberMaker.name))
time.sleep(2.5)

while True:
    #time.sleep(0.01)
    guess = numberGuesser.guess()
    print("\n{0}: {1}".format(numberGuesser.name,guess))
    if guess != num:
        if guess > num:
            print("{0}: {1}".format(numberMaker.name,"Smaller than {0}".format(guess)))
        
        continue
    else:
        print("{0}: {1}".format(numberMaker.name,"yes"))
        break


input()
