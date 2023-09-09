print("Welcome to the tip calcuator!\n")
bill=float(input("What was the total bill? $"))
tip=float(input("What percentage of tip would you like to give? 10, 12, or 15? "))
total=bill+((tip*bill)/100);
persons=int(input("How many people to split the bill? "))
bill_per_person=round(total/persons,2)
print(f"Each person should pay ${bill_per_person}");