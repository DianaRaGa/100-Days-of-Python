print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first = input('''You have landed on a deserted island searching for a treasure
What path will you take? left for the palm trees or right to the caves
Please answer left or right''').lower()
if first == "left":
    print('''You have reached the palm trees.
There is a small lake and next to a rock you found a letter. 
The letter tells you to wait until the sun sets and DO NOT SWIM IN THE LAKE.
    ''')
else:
    print('''Oh no, you found a pack of hungry wolfs taking shelter in the caves
GAME OVER''')
    quit()
second = input("What do you do? wait or swim?").lower()
if second == "wait":
    print('''You have waited for the sunset.
Once the horizon was coloring orange you notice that over the other side of the lake are lights.
You walk over there and found an old cabin.
Once you go inside there are 3 doors of different colors: Red, Blue and Yellow.
    ''')
else:
    print('''You have decided to swim. Big mistake, as soon as you entered the lake you notice that is full of piranhas,
The lake is full of them and you ended up eaten by them
GAME OVER
    ''')
    quit()
three = input("What door do you chose to go through?").lower()
if three == "yellow":
    print('''Congratulations!!! you have found the treasure: A good meal and a sack of gold
Know how will you get it all to your house? 0-0''')
elif three == "red":
    print('''You ended burned completely by a dragon
GAME OVER''')
    quit()
elif three == "blue":
    print('''You entered in the Blue door and...
There is a hipo in the room, you try to run but he is to fast
GAME OVER''')
    quit()
else:
    print(f'''You decided to {three}. Clever but not enough, the floor is lava and you have no scape
GAME OVER''')
    