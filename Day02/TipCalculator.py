print("Welcome to the tip calculator.")

totalBill=float(input("What was the total bill?$"))

tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))

tip_with_Bill=totalBill+((tip/100)*totalBill)

split=int(input("How many people to split the bill?"))

final_pay=round(tip_with_Bill/split,2)

print(f"${final_pay}")