"""
A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.
"""

a = input("enter a number : ")
b = int(a)
total = 0

for i in a :
    total += int(i)
    
if b%total :
    print(a,"a number is not Harshad!!!")
            
else:
    print(a,"a number is a Harshad...")
