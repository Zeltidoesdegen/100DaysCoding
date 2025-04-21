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

player_choice = [rock, paper, scissors]
random_choice = random.randint(0, 2)
computer_choice = player_choice[random_choice]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
if user_choice == 0:
    player_choice = rock
    if random_choice == 0:
        print(f'{player_choice} \n and \n {computer_choice} \n It\'s a draw')
    elif random_choice == 1:
        print(f'{player_choice} \n and \n {computer_choice} \n You Lose!')
    elif random_choice == 2:
        print(f'{player_choice} \n and \n {computer_choice} \n You Win!')
elif user_choice == 1:
    player_choice = paper
    if random_choice == 0:
        print(f'{player_choice} \n and \n {computer_choice} \n You Win!')
    elif random_choice == 1:
        print(f'{player_choice} \n and \n {computer_choice} \n It\'s a draw')
    elif random_choice == 2:
        print(f'{player_choice} \n and \n {computer_choice} \n You Lose!')
elif user_choice == 2:
    player_choice = scissors
    if random_choice == 0:
        print(f'{player_choice} \n and \n {computer_choice} \n You Lose!')
    elif random_choice == 1:
        print(f'{player_choice} \n and \n {computer_choice} \n You Win!')
    elif random_choice == 2:
        print(f'{player_choice} \n and \n {computer_choice} \n It\'s a draw')
else:
    print("Please choose again.")

# Notes to self
# Refactor when you are good.