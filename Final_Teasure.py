print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to the treasure Island.")
print("""Welcome to Treasure Island, a place shrouded in mystery, danger, and untold riches. Long ago, the island was ruled by a fierce pirate king who amassed a fortune beyond imagination. Before he disappeared, he buried his treasure deep within the island, hiding it behind deadly traps, mystical creatures, and enchanted doors. For centuries, brave adventurers have journeyed to the island in search of the legendary treasure, but none have returned... until now.

You are the latest adventurer to set foot on this cursed land. Armed with only your wits and courage, you must navigate through the island's dangers to uncover the pirate king's hidden fortune. But beware—one wrong step could lead to your doom. Choose your path wisely, and perhaps, you'll be the first to claim the treasure that so many have failed to find.""")
print("Your Mission is to find the treasure.")
walk = input("Start of the game.. You have 2 paths ahead. So choose wisely Where do you want to go? LEFT or RIGHT? ").lower()
if walk == "right": 
   print("You walk right into the trap of the adivasiGame Over")       
elif walk == "left": 
    walk = input("DO you want to swim or wait?")
    if walk == "swim":
        print("Game Over")
    elif walk == "wait":
        walk = input("Which door? RED , BLUR , YELLOW ?")
        if walk == "red":
            print("You are dead asshole")
        elif walk == "yellow":
            print("you are dead asshole")
        elif walk == "blue":
            print("Congradulations you are the winner....")
