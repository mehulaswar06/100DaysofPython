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

user_input=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors "))
print(user_input)

computer_input=random.randint(0,2)

if(user_input==0):
  print(rock)
elif(user_input==1):
  print(paper)
else:
  print(scissors)

print("Computer chose")
print(computer_input)


if(computer_input==0):
  print(rock)
elif(computer_input==1):
  print(paper)
else:
  print(scissors)




if(user_input==1 and computer_input==0 or user_input==0 and computer_input==2 or user_input==2 and computer_input==1):
  print("You Won!")
elif(user_input==0 and computer_input==1 or user_input==2 and computer_input==0 or user_input==1 and computer_input==2):
  print("You lose!")
elif computer_input>user_input:
  print("You lose!")
else:
  print("It's a draw!")
