# lists- collection of ordered, changeable, acepts duplicates

fruits=['mango','banana','orange',"banana"]

# print(fruits)

# aceess elements using indexes
# print(fruits[1])

# loop through a llist
# for fruit in fruits:
#     print(fruit,end=" ")

# print the attributes or methods of an object
# print(dir(fruits)) 
# print(help(fruits))

# lists are changeable 
fruits[0]="cherry"

fruits.append("apple")
fruits.remove("cherry")
fruits.insert(0,"pineapple")
fruits.sort()
fruits.reverse()
# fruits.clear()
# print(fruits.index("apple")) #return index of an item
print(fruits.count("banana"))
print(fruits)