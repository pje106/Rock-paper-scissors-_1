import random

list = ['rock', 'paper', 'scissors']

user= input("which one do you want to choose(rock, paper, scissors)? ")
while user.lower() not in list:
  user = input("which one do you want to choose(rock, paper, scissors)? ")
  print('Wrong Value!')

user = user.lower()
computer = random.choice(list)

print("Computer: " + computer)

if computer == user:
  print("Tie")
elif computer == 'paper':
  if user == 'scissors':
    print('You win!')
  else:
    print('I win!')

elif computer == 'rock':
  if user == 'paper':
    print('You win!')
  else:
    print('I win!')

elif computer == 'scissor':
  if user == 'rock':
    print('You win!')
  else:
    print('I win!')    
# if computer == 'paper' and user == 'paper':
#     print('Tie')
# elif computer == 'rock':
#     if user == 'scissors':
#         print('I win!')
#     else:
#         print('You win.')
# else:
#     print('Tie.')