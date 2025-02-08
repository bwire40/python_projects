# format specifiers= {value:flags} format a value based on whatflags are given

price1=45
price2=45.354
price3= -450.33


# 2 d.p, .3f-3 decimals
print(f"price1 is {price1:.2f}")
print(f"price2 is {price2:.2f}")
print(f"price3 is {price3:.2f}")

# add spaces
print(f"price1 is {price1:10}")
print(f"price2 is {price2:10}")
print(f"price3 is {price3:10}")