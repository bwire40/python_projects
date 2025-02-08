
# counts to 10, stops once it reaches 11
for x in range(1,11):
    # print(x)
    pass

# reverse counting from 10
for count in reversed(range(1,11)):
    # print(count)
    pass

# step 
for count in reversed(range(1,11,2)):
    # print(count)
    pass
# continue-skip over an iteration
# break-break from a loop

# continue
for count in reversed(range(1,11)):
    if count==9:
        continue
    print(count)