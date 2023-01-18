"""
Write a program with total change amount as an integer input, and output the change using the fewest coins,
one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular
and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:
0
(or less than 0), the output is:
No change
Ex: If the input is:
45
the output is:
1 Quarter
2 Dimes
"""

change_due = int(input("How much change is due? "))

print(f"Change due back is {change_due}. ")

dollar_count = 0
quarter_count = 0
dime_count = 0
nickel_count = 0
penny_count = 0

if 0 == change_due:
    print("No Change")

else:

    if 100 <= change_due:
        dollar_count += 1
        change_due -= 100

    if 100 <= change_due:
        dollar_count += 1
        change_due -= 100

    if 100 <= change_due:
        dollar_count += 1
        change_due -= 100

    if 100 <= change_due:
        dollar_count += 1
        change_due -= 100

    if 100 <= change_due:
        dollar_count += 1
        change_due -= 100

    if 25 <= change_due:
        quarter_count += 1
        change_due -= 25

    if 25 <= change_due:
        quarter_count += 1
        change_due -= 25

    if 25 <= change_due:
        quarter_count += 1
        change_due -= 25

    if 10 <= change_due:
        dime_count += 1
        change_due -= 10

    if 10 <= change_due:
        dime_count += 1
        change_due -= 10

    if 5 <= change_due:
        nickel_count += 1
        change_due -= 5

    if 1 <= change_due:
        penny_count += 1
        change_due -= 1

    if 1 <= change_due:
        penny_count += 1
        change_due -= 1

    if 1 <= change_due:
        penny_count += 1
        change_due -= 1

    if 1 <= change_due:
        penny_count += 1
        change_due -= 1

print(f"You still owe {change_due}. ")

if 1 == dollar_count:
    print("1 Dollar")
elif 1 < dollar_count:
    print(f"{dollar_count} Dollars ")
          
if 1 == quarter_count:
    print("1 Quarter")
elif 1 < quarter_count:
    print(f"{quarter_count} Quarters ")

if 1 == dime_count:
    print("1 Dime")
elif 1 < dime_count:
    print(f"{dime_count} Dimes")

if 1 == nickel_count:
    print("1 Nickel")
elif 1 < nickel_count:
    print(f"{nickel_count} Nickel ")

if 1 == penny_count:
    print("1 Penny")
elif 1 < penny_count:
    print(f"{penny_count} Pennies")
    
    
    







