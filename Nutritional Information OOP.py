#9.12 Lab: Nutritional Information (Classes / Constructors)



class FoodItem:

    def __init__(self, name, fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat*9)+(self.carbs*4)+(self.protein*4)*num_servings)
        return calories

    def print_info(self):
        print(f"Nutritional information per serving of {self.name}: \n")
        print(f"Fat: {self.fat:.2f} g ")
        print(f"Carbohydrates: {self.carbs:.2f} g ")
        print(f"Protein: {self.protein:.2f} g ")

if __name__ == "__main__":

    item_name = input("What is the name of your food item? \n")
    if item_name == "Water" or item_name == "water":
        food_item = FoodItem(item_name)
        food_item.print_info()
        print(f"Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f} ")

    else:
        amount_fat = float(input("What is the Fat content per serving? \n"))
        amount_carbs = float(input("What is the Carbohydrate content per serving? \n"))
        amount_protein = float(input("What is the Protein content per serving? \n"))
        num_servings = float(input("How many servings? \n"))

        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item.print_info()
        print(f"Number of Calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f} ")
        print(f"Number of Calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f} ")