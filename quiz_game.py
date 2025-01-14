print("Welcome to my Computer Quiz!")

playing=input("Do you Want to Play? (yes/no) ") # prompt the user if they want to play

# set score 0
score=0

# check if the user typed yes, if not quit program
if playing.lower() !="yes":
    quit()

print("Okay! Let's play :)")

# ask questions
answer=input("What does CPU stand for? ")
# check if answer is correct
if answer.lower()=="central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect answer! Try again.")

# 2

answer=input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect answer! Try again.")

# 3
answer=input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect answer! Try again.")

# 4
answer=input("What does PSU stand for? ")
if answer.lower()=="power supply unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect answer! Try again.")

percentage=(score/4)*100
# print score
print("\n\n_______Your Score______")
print("************************")
print("You got " + str(score) + " Question(s) Correct.")
print("You got " + (str(percentage)) + "%.")
if  percentage < 40:
    print("Fail.\n")
else:
    print("Pass.\n")
