"""
Calculate whether a number is a prime number
"""
n = int(input("number : "))
counter = 0
if n >= 0:
    
    for i in range(2,n):
        if n == 0 or n == 1:
            print(n,"is not a prime number")
            break
        elif n%i == 0:
            counter +=1
            break
         if n != 0 and n != 1 and counter == 0 :
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
else:
    print("Please enter a positive number!!!")

