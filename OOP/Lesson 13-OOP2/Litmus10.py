number = int(input("Enter an integer greater than 1: "))
X = 2 
Count = 0
while number > 1:
    multi = False
    while number % X == 0:
        if not multi:
            print(X)
        Count += 1
        multi = True
        number = number // X
    X += 1
print(Count)
        
