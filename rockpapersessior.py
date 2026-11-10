import random
choices=["rock","paper","scissors"]
player=input("Choose rock,paper,or scissors:").lower()
computer=random.choice(choices)
print("You chose:",player)
print("Computer Chose:",computer)
if player not in choices:
    print("Invalid choice! please try again") 
elif player == computer:
    print("It's draw!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
elif player == "rock" and computer == "scissors":
    print("You win!")
else:
    print("computer wins!")