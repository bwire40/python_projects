# execute code while some condition remains true

name=input("Enter your name:\n")
while name=="":
    print("You did not enter your name!")
    name=input("Enter your name please: \n")

if name.isdigit():
    print(f"Your name is a number!")
else:
    print(f"Your name is {name}")