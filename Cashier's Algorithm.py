denominations = [.01, .05, .10, .25, 1.00, 5.00, 10.00, 20.00, 50.00, 100.00]


def transaction_delta(change, denominations):
    change_out = [0] * len(denominations)
    for i, denom in reversed(list(enumerate(denominations))):
        while denom <= change:
            change = change - denom
            change_out[i] += 1
    return(change_out)


item_cost = float(input("Enter the item cost: \n"))
amt_tendered = float(input("Enter the amount tendered: \n"))

change_back = amt_tendered - item_cost


print(f"Change Due: {change_back:.2f} \n")
print(f"1C    5C   10C    25C   1$    5$   10$   20$   50$   100$ \n")
print("     ".join(map(str, transaction_delta(change_back, denominations))))