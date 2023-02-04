tile_dict = {
'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}


user_input = input("Enter a word to see the scrabble value: \n").upper()


def scrabble_score(user_input):
    user_word = user_input
    score = 0
    for letter in user_word:
        score += tile_dict[letter]
    print(f" {user_word} is worth {score} points. \n")
    return score


if __name__ == "__main__":

    scrabble_score(user_input) 