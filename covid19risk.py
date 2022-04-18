print("Yes or No")
age = input("Are you a cigarette addict older than 75 years old?").title()
chronic = input("Do you have a severe chronic disease?").title()
immune = input("Is your immune system too weak?").title()
risk = age or chronic or immune

if risk == "Yes":
    print("You are in risky group.")
elif risk == "No":
    print("You aren't in risky group.")
