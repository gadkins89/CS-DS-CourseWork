def the_great_divide(num1, num2):

    #aufteilung = num1 / num2
    try:
       aufteilung = num1 / num2
    except  ZeroDivisionError as zde:
        print("ZeroDivisionError:", str(zde))
    except ValueError as ve:
        print(str(ve))
    return aufteilung


if __name__ == "__main__":
    try:
        user_num = int(input("Enter a dividend: "))
        div_num = int(input("Enter a divisor: "))
    except ValueError as ve:
        print("ValueError:", str(ve))
    
    try:
        print(the_great_divide(user_num, div_num))
    except NameError as ne:
        print("NameError:", str(ne))