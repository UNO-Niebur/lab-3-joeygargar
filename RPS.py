#RPS.py
#Name:Mia Garcia
#Date:2/12/26
#Assignment:Lab 3 
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  playagain = "Y"
  while playagain == "Y":

    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice (["R","P","S"])

   #Prompt the user for their RPS selection
    player = input("choose your weapon (R, P, S):")

    #Determine winner and state what happened to the user
    if computer == "R":
       print("computer chose rock")
       if player == "R": 
        ties = ties + 1
        print("tie")
       elif player == "P":
        wins = wins + 1
        print("player wins")
       elif player == "S": 
        losses = losses +1 
        print("computer wins")

    elif computer == "P":
      print("computer chose rock")
      if player == "P":
        ties = ties + 1 
        print("tie")
      elif player == "R":
        losses = losses + 1 
        print("computer wins")
      elif player == "S":
        losses = losses + 1
        print("player wins")
    
  

    else: 
      print("computer chose scissors")
      if player == "R":
        wins = wins + 1 
        print("player wins")
      elif player == "P":
        losses = losses + 1 
        print ("computer wins")
      elif player == "S":
        ties = ties + 1
        print("tie")

    

      
  #Ask the user if they would like to play again.
    playagain = input("play again? (Y/N)")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
