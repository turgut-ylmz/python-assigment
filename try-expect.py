fruit = ["banana","mango","pear","apple","kiwi"]
counter = 3

while counter > 0 :
    
    try :
        print(f"You have {counter} right.")
        index = int(input("Pick an index number : "))
        print("Your favoirete fruit is :",fruit[index])
    except IndexError :
        counter -= 1
        print(f"Index error raised. You have {counter} right left. Try again!")
    except ValueError :
        counter -= 1
        print(f"Value error raised. You have {counter} right left. Try again!")
    else:
        print("Congrats! You've entered valid input.")
        break
    finally:
        print("Our fruits are always fresh!")
