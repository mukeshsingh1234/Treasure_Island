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
print("Welcome to Treasure Island.\nYour mission is to find the treasure")

direction = input("You have two roads, where would you go? Left or Right\n")
direction = direction.lower()
if direction == "left":
    print("Congrates! You Just saved yourself!\n")
    way = input("Now would your rather swim or wait for the boat to arrive in a lonely Lake? swim or wait\n")
    way = way.lower()
    if way == "wait":
        print("You are one lucky person, Your option Just saved your life!\n")
        door = input("You have 3 door infront of you, whioch would you choose? Red, Yello or Blue?\n")
        door = door.lower()
        if door == "red" or "Blue":
            print("Unlucy, you are dead! GAME OVER!\n")
        else:
            print("Congrats, you ahve successfully completed the Game! Enjoy!\n")
    else:
        print("You just got eaten by deadly deep water creatures. GAME OVER!\n")
else:
    print("Game Over!, You went in the wrong way!\n")
