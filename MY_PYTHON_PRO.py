print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' What is CPU stands for? \n ')
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' What is GPU stands for? \n ')
if answer.lower() == 'graphical processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is RAM stands for? \n ')
if answer.lower() == 'random access memory':
    print("Correct")
    score += 1
else:
    print('Wrong')
