import math

# calculate hypotnuse
# 
# |\ 
# | \
# |  \
# |   \
# |a   \c
# |     \
# |      \
# |___b___\ 


length= float(input("Enter length a:\n"))
base= float(input("Enter base b:\n"))

# c=sqr of a²+b²
c=math.sqrt(pow(length,2)+pow(base,2))

print(f"Side c is {round(c,2)} cm")

# calcualte the area of a cicle

