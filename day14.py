from getpass import getpass as input

player_1 = input("Player 1 please select R, P, or S")
print("Let's see what you got Player 2!")
player_2 = input("Player 2 please select R, P, or S")

if player_1 == "R" and player_2 == "P":
    print("Player 2 is the winner!")
elif player_1 == "P" and player_2 == "R":
    print("Player 1 is the winner!")
elif player_1 == "S" and player_2 == "R":
    print("Player 2 is the winner!")
elif player_1 == "R" and player_2 == "S":
    print("Player 1 is the winner!")
elif player_1 == "P" and player_2 == "S":
    print("Player 2 is the winner!")
elif player_1 == "S" and player_2 == "P":
    print("Player 1 is the winner!")
else:
    print("It's a tie!")
