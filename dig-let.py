"""
Program that accepts a string and calculate the number of digits and letters.
"""

word = input("enter something  : ")
digit = 0

for i in word:
    if i.isdigit() :
        digit += 1

print("Digit : ",digit,"\nLetter : ",(len(word)-digit))
