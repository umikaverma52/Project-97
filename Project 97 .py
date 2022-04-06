import  random
win1=0
randomNo=random.randint(1,9)
chances=0
while (chances<=5):
    guess=int(input("Pls enter your guess number"))
    chances=chances+1
    if(guess<randomNo):
        print("Your guess is less than the randomn number")
    elif(guess>randomNo):
        print("Your guess is more than the randomn number")
    else:
        print("Congratulation!")
        win1=1
        break
if(win1==0):
    print("You Lost!")
    