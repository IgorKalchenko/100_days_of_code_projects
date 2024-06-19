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
step1 = input('First you need to decide where to go? Left or Right? \n').lower()
if step1 == "left":
    print("Wow! That's marvelous! You're moving to a lake")
    step2 = input("Now you are at the shore of the island. So you have to decide whether wait for a boat or swim "
                  "right now. What is your choice: swim or wait? \n").lower()
    if step2 == "wait":
        print("You are damn good at strategy man! You finally came to a castle.")
        step3 = input(
            "Here is the castle with 3 doors: red, yellow and blue. Which one will you enter? Choose wisely! \n").lower()
        if step3 == "red":
            print("Ooops. You've been burned by fire. Game over(((")
        elif step3 == "blue":
            print("Well... You've been eaten by terrible beasts. For you it's the end.")
        elif step3 == "yellow":
            print("You find the treasure! You win!!!")
        else:
            print("Something went wrong. Think about it. Game over.")
    else:
        print("I hate to tell you this but you've been attacked by trout. Game over(((")
else:
    print("My condolences. You fall into a black hole. RIP.")