weight_1 = float(input("Enter weight 1: \n"))
weight_2 = float(input("Enter weight 2: \n"))
weight_3 = float(input("Enter weight 3: \n"))
weight_4 = float(input("Enter weight 4: \n"))

weights_list = [weight_1, weight_2, weight_3, weight_4]

average_weight = sum(weights_list) / len(weights_list)

max_weight = max(weights_list)

format_average = "{:.2f}".format(average_weight)
format_max = "{:.2f}".format(max_weight)

print(f"Weights: {weights_list}")
print(f"Average Weight: {format_average}")
print(f"Max Weight: {format_max}")

list_location = input("Enter a list location (1 - 4): \n")

if list_location == "1":
    print(f"Weight in pounds: {weights_list[0]:.2f}")
    print(f"Weight in kilograms: {weights_list[0] / (2.2):.2f}")
elif list_location == "2":
    print(f"Weight in pounds: {weights_list[1]:.2f}")
    print(f"Weight in kilograms: {weights_list[1] / (2.2):.2f}")
elif list_location == "3":
    print(f"Weight in pounds: {weights_list[2]:.2f}")
    print(f"Weight in kilograms: {weights_list[2] / (2.2):.2f}")
else:
    print(f"Weight in pounds: {weights_list[3]:.2f}")
    print(f"Weight in kilograms: {weights_list[3] / (2.2):.2f}")

weights_list.sort()
print(f"Sorted List: {weights_list}")

