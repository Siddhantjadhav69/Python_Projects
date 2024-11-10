import random

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
images = [rock, paper, scissors]

user = int(input("Let's Begin! so 0 for rock 1 for paper and 2 for scissors. \n"))

if user >= 3 or user <= 0:
    print("you type an invalide number you lose.")
else:
    print(images[user])
    computer = random.randint(0,2)
    print(images[computer])

    if user == 0 and computer == 2:
     print("You win!")
    elif computer == 0 and user == 2:
     print("you loose")
    elif computer > user:
     print("You lose!")
    elif user > computer:
     print("You win!")
    elif computer == user:
     print("Thst's a draw!")
