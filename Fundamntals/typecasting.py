# typecasting-convert a variable from one data ytpe to another
# str(),float(),int(),bool()

name="bwire"
age=25
gpa=3.5
is_student=True

print(type(name)) # str
print(type(age)) # int
print(type(gpa)) # float
print(type(is_student)) # boolean

# foat to int
gpa=int(gpa) 

# int to float
age=float(age) # float

# int to str
age=str(age) # string


# text to bool 
# bolean only returns false if the variable is empty/null
name=bool(name)

print(f"Results: ",gpa,type(gpa))
print(f"Results: ",age,type(age))
print(f"Results: ",name,type(name))
