#Rock-Paper-Scissors game zuri
#using random class
import random

'''
A brief summary:

If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
'''

#list to store all possible options
Options_list = ["R","P","S"]
Options_dict = {"R":"Rock", "P":"Paper", "S":"Scissors"} #dictionary of options to show actual character in display


#function to determine if player wins CPU by returning "win" when player wins or "loss" when player loses
def check_move(Player_Option, CPU_Option):
    if ( Player_Option == "R") and (CPU_Option == "S"):
        return "Win"
    elif ( Player_Option == "P") and (CPU_Option == "R"):
        return "Win"
    elif ( Player_Option == "S") and (CPU_Option == "P"):
        return "Win"
    else:
        return "Loss"

#Main program body
CPU_Choice = random.choice(Options_list) #code to determin CPU choice using the choice function of random class
Player_Choice = str(input("Choose Character: R for Rock P for Paper S for Scissors ==> ")) #Code to take player input

#loop until user enter R P or S
while (Player_Choice != "R" and Player_Choice != "P" and Player_Choice != "S"):
    print(f"{Player_Choice} is not a valid option")
    Player_Choice = str(input("Choose Character: R for Rock, P for Paper, S for Scissors ==> "))

while (Player_Choice == CPU_Choice):
    #when there is a tie, the program will rerun and provide guidance for Player to choose a character
    print(f"Player ({Options_dict[Player_Choice]}) : CPU ({Options_dict[CPU_Choice]}) is a tie")
    Player_Choice = str(input("Choose Character: R for Rock, P for Paper, S for Scissors ==> "))
else:
    print(f"You selected {Options_dict[Player_Choice]}") #Code to display user selection
    if check_move(Player_Choice, CPU_Choice) == "Win":
        print(f"Player ({Options_dict[Player_Choice]}) wins CPU ({Options_dict[CPU_Choice]})") 
    else:
        print(f"Player ({Options_dict[Player_Choice]}) Loses to CPU ({Options_dict[CPU_Choice]})")
 


    

