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

#Write your code below this line 👇
import random

player = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors\n"))
if player == 0:
  print(rock)
elif player == 1:
  print(paper)
else :
  print(scissors)

print("Computer chose")
comp = random.randint(0,2)
if comp == 0:
  print(rock)
elif comp == 1:
  print(paper)
else :
  print(scissors)

if player == 0:
  if comp == 0:
    print("Draw")
  elif comp == 1:
    print("You lose.")
  else:
    print("You win")
elif player == 1:
  if comp == 0:
    print("You lose.")
  elif comp == 1:
    print("Draw")
  else:
    print("You win")
else :
  if comp == 0:
    print("You win.")
  elif comp == 1:
    print("You lose")
  else:
    print("Draw")