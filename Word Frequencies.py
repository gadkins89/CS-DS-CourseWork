def build_dictionary(words):
    my_dictionary = {}
    for i in words:
        if i in my_dictionary:
            my_dictionary[i] += 1
        else:
            my_dictionary[i] = 1
    return my_dictionary


        

if __name__ == "__main__":

    words = input("Enter a series of words to check word frequency: \n").split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(f" {key} - {str(your_dictionary[key])}")