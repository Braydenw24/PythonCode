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
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You decide a treasure-hunting vacation is in order. Rumors are that Captain Black\nSam's long lost treasure is on the cusp of being discovered and will make the people who find it rich for a thousand lifetimes...\n")

destination = input("The rumors indicate that there are three loacaions where the treasure could be. Where do you want to go Maui, Europe, or the Mediterranean? ")

if destination == "Maui" or "Europe" or "the Mediterranean":
  travel_method = input("\nDo you want to fly, take a boat, or teleport? ")


if travel_method =="fly" and destination =="The Mediterranean":
    print("\nYou fly to the harbor and board your cruise; soon after, you arrive at the island where\nCaptain Black Sam's treasure is rumored to be...")
    walk_search = input("\nAt the island, do you want to walk the coastline or search the forest? ")
    if walk_search == "Walk the coastline.":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "Walk the coastline":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "walk the coastline.":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "walk the coastline":
      print("\nYou walk the coast until you starve. Game over... try again?")
    else:
        print("\nYou search the forest and find the treasure. Congratulations, you win!")

  
if travel_method == "boat" and destination =="The Mediterranean":
    print("\nYou board a small cruiser and arrive at an the island rumored to hold\nCaptain Black Sam's treasure. ")
    walk_search = input("\nAt the island, do you want to walk the coastline or search the forest? ")
    if walk_search == "Walk the coastline.":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "Walk the coastline":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "walk the coastline.":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "walk the coastline":
      print("\nYou walk the coast until you starve. Game over... try again?")
    else:
        print("\nYou search the forest and find the treasure. Congratulations, you win!")

if travel_method == "teleport" and destination =="The Mediterranean":
    print("\nYou teleport into the middle of the ocean, then swim to a mysterious island and smell\ntreasure nearby... perhaps it's the salt.")
    walk_search = input("\nAt the island, do you want to walk the coastline or search the forest? ")
    if walk_search == "Walk the coastline.":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "Walk the coastline":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "walk the coastline.":
      print("\nYou walk the coast until you starve. Game over... try again?")
    elif walk_search == "walk the coastline":
      print("\nYou walk the coast until you starve. Game over... try again?")
    else:
        print("\nYou search the forest and find the treasure. Congratulations, you win!")


if travel_method  == "fly" and destination == "Maui":
    print("\nDue to a natural disaster, all flights are delayed. By the time you're able to get a\nflight, your Boss wants you back in the office. Try again?")

elif travel_method == "teleport" and destination == "Maui":
      print("\nYou sneak into Area 51, pass the soldiers, activate the teleporter and scream\n"+'"Beam me up, Scotty!"'+ " Soon after, you arrive on a dark strange planet and hear a\nmenacing growl creep behind you. Game over... try again? ")

elif travel_method == "boat" and destination == "Maui":
    print("\nYou arrive on The Intacti, find a lover named Jack or Jill, hit an iceberg, and both\nsurvive the ship sinking because you decided to share the extra space on a floating door you found with your significant other. In the end, you don't find the treasure.\nTry again?")


if travel_method =="fly" and destination == "Europe":
    print("\nAs you board your flight, everything goes smoothly; upon flying over Europe,\nturbulence increases tenfold, and Russia fires missiles at your aircraft mistaking\nyour airplane for a Ukrainian supply plane.  Try again?")

elif travel_method == "boat" and destination == "Europe":
    print("\nYou arrive on The Intacti, find a lover named Jack or Jill, hit an iceberg, and your\nsignificant other goes snorkling even if there is enough room on the door for the\nboth of you. Game over... Try again?")

elif travel_method == "teleport" and destination == "Europe":
      print("\nYou sneak into Area 51, pass the soldiers, activate the teleporter and scream\n" + '"Beam me up, Scotty!"' + " Soon after, you arrive on a dark strange planet and hear a\nmenacing growl creep behind you. Game over... try again? ")
