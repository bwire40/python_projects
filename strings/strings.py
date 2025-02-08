# string methods

name="emmanuel bwire"

# print(len(name)) #print the length of the string (14)-includesspaces

#find first position of a character at position 8(index 8)
# print(name.find(" ")) 
# print(name.capitalize())  #capitalize
# print(name.upper()) #uppercase
# print(name.lower())
# print(name.isdigit()) #checks if string is digit
# print(name.isalpha()) # checks if string is only alphabetcal
# print(name.isnumeric()) #If name is a string consisting entirely of numbers (e.g., "1234"), it will return True
# print(name.count("e")) #count() method in Python is used to count how many times a specified value appears in a string or a list
# print(name.replace('e','i'))  #replace a specified substring with another substring in a string.

# print(help(str))


# string indexing
print(name[0])
credit_card_number="1234-5678-9123"
print(f"The credi card number is XXXX-XXXX-{credit_card_number[-4:]}")