#9.11 Lab: Car Value (Classes)



class Car:

    def __init__(self, model_year, purchase_price, current_value):
        self.model_year = model_year
        self.purchase_price = purchase_price
        self.current_value = current_value

    def calculate_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        print(f"Model Year:", self.model_year)
        print(f"Purchase Price:", "$",self.purchase_price)
        print(f"Current Value:", "$",self.current_value)
        

if __name__ == "__main__":
    year = int(input("Please enter the year your vehicle was new: \n"))
    price = int(input("Please enter the purchase price of your vehicle: \n"))
    current_year = int(input("Please enter the current year: \n"))

    my_car = Car(year, price, current_year)
    my_car.calculate_current_value(current_year)
    my_car.print_info()