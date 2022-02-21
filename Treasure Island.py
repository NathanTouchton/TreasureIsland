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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

pre_one = input("You wake up in a dark dungeon. You quickly get over the thought of how cliche that is, and start looking for a way out. You see two paths: one going left, and one going right. Which way to you take? ")

one = pre_one.lower()

if one == "left":
    print("You decide to go left, continuing into the darkness.")
    pre_two = input("After going down a long corridor for what seems like ages, you find yourself on a shoreline outside the dungeon. There's no paths except into the water. It's night time, but you think you can vaguely see some lights in the distance on the other side of the water. You might be able to swim, but it's hard to tell how far it is. Do you swim or wait to flag down a boat when it gets a bit brighter? (Type 'swim' or 'wait') ")

    two = pre_two.lower()
    if two == "wait":
        pre_three = input("After some waiting, you manage to flag down a boat going past. They bring you back to the harbor, but you are still not sure where you are. You wander into a nearby building just outside town to ask for assistance, but the building looks abandoned. The door locks behind you as you walk in. How convenient! Ahead there are 3 doors. One red, one yellow, one blue. Which door do you try? (Type the color only.) ")

        three = pre_three.lower()

        if three == "yellow":
            print("The door is unlocked. You not only find a way out, but you also find a massive amount of lost treasure on the way! It seems no one knows about it, so you should be able to come back here after you find your way back home to stuff as much as you can in your car. Congratulations! You win!")
        elif three == "blue":
            print("You go through the blue door. On the other side, you think you hear some growling. There's some wild beasts who have made their den in this room of the building. The mom of these beasts attacks you and feeds you to her childeren. Well, that could have gone better.")
        elif three == "red":
            print("You walk through the red door. There's a piece of gold on a pedestal. You take it. You're rich! Unfortunately, whoever left this here watched too much Indiana Jones, and left a trap. On your way out, a bucket of flaming oil falls on your head. Honestly, it was quite the spectacle! You're still dead though.")
    else:
        print("You try swimming across the lake. You drown like a stupid lemming.")
else:
    print("You go right. You don't make if far before you fall down what seems to be a mineshaft of some sort. Game Over!")


# pre_two = input("After going down a long corridor for what seems like ages, you find yourself on a shoreline outside the dungeon. There's no paths except into the water. It's night time, but you think you can vaguely see some lights in the distance on the other side of the water. You might be able to swim, but it's hard to tell how far it is. Do you swim or wait to flag down a boat when it gets a bit brighter? (Type 'swim' or 'wait' ")

# two = pre_two.lower()

# pre_three = input("After some waiting, you manage to flag down a boat going past. They bring you back to the harbor, but you are still not sure where you are. You wander into a nearby building just outside town to ask for assistance, but the building looks abandoned. The door locks behind you as you walk in. How convenient! Ahead there are 3 doors. One red, one yellow, one blue. Which door do you try? ")

# three = pre_three.lower()