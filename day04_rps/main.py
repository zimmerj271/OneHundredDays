from random import randint

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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
choice = int(choice)
while choice < 0 or choice > 2 or type(choice) is not int:
    choice = input("Please enter an integer, 0 for Rock, 1 for Paper, 2 for Scissors")
computer_choice = randint(0,2)
selection = [rock, paper, scissors]
selection_text = ['Rock', 'Paper', 'Scissors']

if (choice == 0 and computer_choice == 2) or (choice > computer_choice) and not (choice == 2 and computer_choice == 0):
    print(selection[choice], '  ', selection[computer_choice])
    print(selection_text[choice], ' beats ', selection_text[computer_choice], ', You WIN!!!')
elif (choice == 2 and computer_choice == 0) or (choice < computer_choice) and not (choice == 0 and computer_choice == 2):
    print(selection[choice], '  ', selection[computer_choice])
    print(selection_text[computer_choice], ' beats ', selection_text[choice], ', You Lose...')
elif choice == computer_choice:
    print(selection[choice], '  ', selection[computer_choice])
    print(selection_text[choice], ' and ', selection_text[computer_choice], ', Tie.')
