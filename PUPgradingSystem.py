#  Another program! If function, elif, and else will be used?
import math

def Equivalent():
    grade = float(input("What is your exact average: "))
    Final_= math.ceil(grade) 
    if 97 <= Final_ <= 100:
        print("You got 1.00 as your average")
        print("'Excellent'")
    else: 
        94<= Final_ <= 96
        print("You got 1.25 as your average")
        print("'Excellent'")

Equivalent()

