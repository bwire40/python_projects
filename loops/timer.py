import time

# time.sleep(3) #delay execution of a program for the specified time

my_time=60 # in seconds

for x in range(my_time,0,-1):
    seconds=x%60
    print(x)
    time.sleep(1)
    print(f"{seconds}")