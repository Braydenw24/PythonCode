#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What is your total dining bill? $"))
percent_tip = int(input("How much do you want tip? 10, 12, 15, or 20 percent? %" ))
how_many_going_Dutch = int(input("How many people are going to split the bill? "))
what_to_leave =(total_bill/how_many_going_Dutch)*(1+(percent_tip/100))

#To get the 33.60 instead of using the round function
final_amt =  "{:.2f}".format(what_to_leave)
print(f"Everyone pays: ${final_amt}")

bill_with_tip = percent_tip / 100 * total_bill + total_bill
print(f"The total bill for your table is ${round(bill_with_tip,2)}.")

