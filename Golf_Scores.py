
"""
Golf scores record the number of strokes used to get the ball in the hole.
The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5).
Each score's name is based on the actual strokes taken compared to par:
"Eagle": number of strokes is two less than par
"Birdie": number of strokes is one less than par
"Par": number of strokes equals par
"Bogey": number of strokes is one more than par
Given two integers that represent par and the number of strokes used, write a program that prints
the appropriate score name. Print "Error" if par is not 3, 4, or 5.

"""

strokes = int(input("How many strokes did you take? "))
print(f"You took {strokes} strokes. ")

par = int(input("How many strokes is par for this hole? "))
print(f"The par for this hole is {par} strokes. ")

stroke_difference = par - strokes
print(f"The difference in strokes is: {stroke_difference} ")

if 2 == stroke_difference:
    print("Eagle")
elif 1 == stroke_difference:
    print("Birdie")
elif 0 == stroke_difference:
    print("Par")
elif -1 == stroke_difference:
    print("Bogey")
else:
    print("Error")











