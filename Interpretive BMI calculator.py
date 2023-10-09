# Body Mass Index Calculator

height = float(input("What is your height in meters? "))
weight = int(input("What is your weight in kilograms? "))
bmi = weight/(height*height)

print("")

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25.0:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25.0 and bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30.0 and bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 35.0:
  print(f"Your BMI is {bmi}, you are clinically obese.")