#  Finding the lowest number among the three inputted values

def Lowest_Value(a,b,c):
    if a > b > c:
        print(c)
    else:
        if a < b > c:
            print (a)
        else:
            print (b)

print(Lowest_Value(25, 38 , 13))