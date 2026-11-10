ISBN = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for count in range(13):
    ISBN[count] = int(input("enter next digit of ISBN: "))

CalculatedDigit = 0
count = 0

while count < 12:
    CalculatedDigit = CalculatedDigit + ISBN[count]
    count += 1
    CalculatedDigit += ISBN[count] * 3
    count += 1

while CalculatedDigit >= 10:
    CalculatedDigit -= 10
    
CalculatedDigit = 10 - CalculatedDigit 
if CalculatedDigit == 10:
    CalculatedDigit = 0

if CalculatedDigit == ISBN[12]:
    print("valid ISBN")
else:
    print("invalid ISBN")
