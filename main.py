#Guessing game
import random
n = random.randint(1,100)
guess = -1
attempts =0
while(guess != n):
    guess = int(input("Guess the number:"))
    attempts+=1
    if(guess>n):
        print("Lower number Please")
    elif(guess<n):
        print("Higher number please")
    else:
       print(f"You guessed it in {attempts} attempt.") 





