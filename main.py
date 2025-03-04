'''
1 for rock
0 for paper
-1 for scissors
'''
import random   # importing random module
computer = random.choice([-1,1,0])  
youstr = input("Enter your choice: ")
youDict= {"r":1 , "p":0, "s":-1}
you = youDict[youstr]
reverseDict = {1:"Rock", 0:"Paper", -1:"Scissors"}
# by now we have two varibles computer and you

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]} ")

if computer == you:
  print("Draw")
else:
  if(computer==-1 and you==1): 
    print("You win")
  elif(computer==1 and you==-1):
    print("You lose")
  elif(computer==0 and you==1): 
    print("You lose")
  elif(computer==1 and you==0): 
    print("You win")
  elif(computer==-1 and you==0):
    print("You lose")
  elif(computer==0 and you==-1):
    print("You win")
  else:
    print("Invalid input")
