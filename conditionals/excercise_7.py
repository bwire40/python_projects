# python calculator


# user input
operator=input("Enter an operator (+,-*,/): \n")
# checks
if operator !='+' and operator!="-" and operator!='*' and operator!='/':
    print(f"{operator} is Invalid!.")
else:
    num1=float(input("Enter the first number: \n"))
    num2=float(input("Enter the second number: \n"))
    if operator =='+':
        result=num1+num2
        print(f"You chose {operator}.\nThe answer is {round(result,2)}")
    elif operator =='-':
        result=num1-num2
        print(f"You chose {operator}.\nThe answer is {round(result,2)}")
    elif operator =="*":
        result=num1*num2
        print(f"You chose {operator}.\nThe answer is {round(result,2)}")
    elif operator=="/":
        result=num1/num2
        print(f"You chose {operator}.\nThe answer is {round(result,2)}")
    else:
        print("Try again!")