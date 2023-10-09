#Nested if/else and else if statement: Rollercoaster

print("Welcome to Mickey Mouse's rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride this rollercoaster.")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.00.")
  elif age <=18:
    print("Please pay $7.00.")
  else:
    print("Please pay $12.00.")
else: 
  print("I am sorry, but you are not tall enough to ride the rollercoaster.")