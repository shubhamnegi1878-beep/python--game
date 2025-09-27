#SNAKE--WATER--GUN
import random
''' # game controls 
1 for snake  
-1 for water 
0  for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")
else:
    print("You lose!")