print("Welcome to the tipping system? ")
bill = float(input("How much are you going to pay? "))
tip = int(input("How much tip are you going to leave? "))
people = int(input("How many people are going to pay? "))


tip_percent = tip / 100
total_bill_amount = bill * tip_percent
total_bill = bill + total_bill_amount
bill_for_person = total_bill / people

final_amount = round(bill_for_person, 2)
print(final_amount)