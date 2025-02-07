#  shopping cart program, item,quantity,price

item=input("What is the items you like to buy?: \n")
price=float(input("Whats the price?:\n"))
quantity=int(input("quantity:\n"))

# calculate
total=price*quantity

# print
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")