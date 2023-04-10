import random
num = random.randint(1,10)
print("I'm thinking of a number from one to ten.")
while True:
    guess = int(input(">"))
    if guess != num:
        print("no")
        continue
    else:
        print("yes!")
        break
