# tip Calculator
print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))       # input always give str datatype
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or20? "))
ppl = int(input("How many people to split the Bill? "))

tip = bill*tip_percent/100
total_bill = bill + tip
bill_per_person = round(total_bill/ppl,2)
final_amt = "{:.2f}".format(bill_per_person)  # doubt
print(f"Each person should pay : ${final_amt}")
