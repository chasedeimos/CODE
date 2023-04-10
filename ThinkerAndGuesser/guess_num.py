input("Think of a number from 1 to 10 and press enter.\nDon't tell me")
while True:
    for num in range(10):
        guess = num
        reply = input("\nIs " + str(guess) + " the number you're thinking about?\n")
        if reply == "no":
            continue
        else:
            print("Awesome, I guessed your number!")
        break
    break
            
            
    
