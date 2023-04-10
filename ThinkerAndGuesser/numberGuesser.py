import random
name = "Guesser"
notnum = []
def guess():
    while True:
        num = random.randint(1,10)
        if num not in notnum:
            notnum.append(num)
            return num
        else:
            continue
