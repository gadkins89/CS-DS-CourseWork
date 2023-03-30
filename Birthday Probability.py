def unique_probability(num_people):
    ''' 
    Finds the probability of unique
    birthdays among a group of people
    and returns the probability of
    shared birthdays among two or more
    people.
    '''
    probability = 1
    for n in range(num_people):
        probability *= ((365-n) / 365)
    return float((1 - probability) * 100)



if __name__ == "__main__":

    num_people = int(input("Enter a number of people: \n"))

    print(f'''
    There is a {unique_probability(num_people):.20g} % chance
    two or more people share a birthday
    ''')