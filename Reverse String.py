"""
5.17 LAB: Print string in reverse
Write a program that takes in a line of text as input, and outputs that line of text in reverse.
The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH
"""

exit_text_1 = "Done"
exit_text_2 = "done"
exit_text_3 = "d"

while True:
    reverse_text = input("Please enter a line of text you would like to reverse.\n")
    for character in range(len(reverse_text) -1, 0-1, -1):
        print (reverse_text[character], end = " ")
        if reverse_text == exit_text_1:
            exit("Goodbye. ")
        elif reverse_text == exit_text_2:
            exit("Goodbye. ")
        elif reverse_text == exit_text_3:
            exit("Goodbye. ")
