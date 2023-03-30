import random

def unique_random_ints(how_many, max_num):
    numbers_generated = [0]
    retries = 0
    while len(numbers_generated) < how_many:
        random_number = random.randint(0, max_num)
        if random_number not in numbers_generated:
            numbers_generated.append(random_number)
        elif random_number in numbers_generated:
            retries += 1
    return f"""Unique numbers generated: {numbers_generated}
Retries after generation of existing number : {retries}"""




if __name__ == '__main__':
    seed = int(input("Enter a seed value to initiate the random module: \n"))
    how_many = int(input("Enter the amount of numbers to generate: \n"))
    max_num = int(input("Enter the upper limit of the number range: \n"))

    random.seed(seed)

    print(unique_random_ints(how_many, max_num))