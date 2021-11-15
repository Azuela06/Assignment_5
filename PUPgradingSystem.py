#  Another program! If function, elif, and else will be used?
import math

def Equivalent():
    grade = float(input("What is your exact average: "))
    print(f"Your grade is {grade}")
    Final_= math.ceil(grade) 
    if 97 <= Final_ <= 100:
        print("You got 1.00 as your average")
        print("Description: EXCELLENT")
    elif(93< Final_ <= 96):
        print("You got 1.25 as your average")
        print("Description: EXCELLENT")
    elif(90 < Final_ <=93):
        print("You got 1.5 as your average")
        print("Description: VERY GOOD")
    elif(87 < Final_ <= 90):
        print("You got 1.75 as your average")
        print("Description: VERY GOOD")
    elif(84 < Final_ <= 87):
        print("You got 2.00 as your average")
        print("Description: GOOD")
    elif(81 < Final_ <= 84):
        print("You got 2.25 as your average")
        print("Description: GOOD")
    elif(78 < Final_ <= 81):
        print("You got 2.5 as your average")
        print("Description: SATISFACTORY")
    elif(75 < Final_ <= 78):
        print("You got 2.75 as your average")
        print("Description: SATISFACTORY")
    elif( Final_ == 75):
        print("You got 3.00 as your average")
        print("Description: PASSING")
    else:
        64 < Final_ <= 74
        print("You got 5.00 as your average")
        print("Description: FAILURE")
    
Equivalent()
