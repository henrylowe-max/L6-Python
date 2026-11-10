

s = ""
while s != "x":
    s = str(input("enter a word or phrase :"))
    Max = len(s) - 1
    matched = True
    for i in range(0,Max):
        letter1 = s[i]
        letter2 = s[Max - i]
        if letter1 != letter2:
            matched = False
    if matched == True:
        print("palindrome")
    else:
        print("not a palindrome")
