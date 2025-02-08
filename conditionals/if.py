#  if = do some code if some condition is True
# elif-add more conditions

# age=int(input("Enter your age:\n"))
response=input("Would you like food?(Y/N)\n")

# if age>=18 and age<100:
#     print("You are of age")
# elif age<0:
#     print("you are not even born")
# elif age>=100:
#     print("you are too old to sign up.")
# else:
#     print("You are not of age")

if response =='Y' or response=='y':
    print("have some food");
elif response =='N' or response=='n':
    print("You dont want food")
else:
    print("Invalid input!")