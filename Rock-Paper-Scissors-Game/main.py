import random
print("Welcome to Rock, Paper, Scissors Game\n")
# Explains player about the winning rules of the game
print("Winning Rules of the Rock, Paper, Scissor Game")
print("are as follows:")
print("Rock vs Scissors-> Rock wins")
print("Scissors vs Paper-> Scissors wins")
print("Paper vs Rock-> Paper wins")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Set initial scores of player and computer to 0
Player_scores = 0
Computer_scores = 0
#Write your code below this line 👇
for i in range(1, 6):
  print()
  print(f"Round: {i}\n")
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
  computer_choice = random.randint(0,2)
  print("Player chose : " + str(user_choice))
  if user_choice == 0 :
     print(rock)
  elif user_choice == 1 :
     print(paper)
  else:
     print(scissors)
  print("Computer chose: " + str(computer_choice))
  if computer_choice == 0:
     print(rock)
  elif computer_choice == 1:
     print(paper)
  else:
     print(scissors)

  if user_choice == 0 and computer_choice == 1:
     print("you loose!")
     Computer_scores +=1
  elif user_choice == 0 and computer_choice == 2: 
     print("you win! ")
     Player_scores +=1
  elif user_choice == 1 and computer_choice == 0:
     print("you win! ")
     Player_scores +=1
  elif user_choice == 1 and computer_choice == 2:
     print("you loose! ")
     Computer_scores +=1
  elif user_choice == 2 and computer_choice == 0:
     print("you loose! ")
     Computer_scores +=1
  elif user_choice == 2 and computer_choice == 1: 
     print("You win!")
     Player_scores +=1
  else:
     print("Tie! ")
  print()
  print(f"Computer_scores: {Computer_scores}")
  print(f"Player_scores: {Player_scores}")
print()
if Player_scores > Computer_scores:
   print("You won the game!")
elif Computer_scores > Player_scores:
   print("Computer won the game!")
else:
   print("Tie game!!!!")
