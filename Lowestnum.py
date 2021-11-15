#  Finding the lowest number among the three inputted values

def Lowest_Value():
    a= int(input("Give a number: "))
    b= int(input("Give another number: "))
    c= int(input("Give another number: "))
    if a > b > c:
        print(c)
    else:
        if a > b < c:
            print (b)
        else:
            a < b < c
            print (a)

Lowest_Value()
