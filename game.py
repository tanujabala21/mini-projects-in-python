
import random 
def guessing_number():
    print("welcome to number guessing game!!")
    print("guess number from 1 to 100")
    number=random.randint(1,100)
    attempts=0
    while True:
        guess=int(input("enter the number:"))
        if guess<number:
            print("Too low!!")
            attempts+=1
        elif guess>number:
            print("Too high!!")
            attempts+=1
        elif guess==number:
            print("yeahh!! you guessed correct!!")
            print(f"you guessed in {attempts} attempts")
            break
        else:
            print("not valid")
guessing_number()