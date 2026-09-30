# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)


dataStr = input("")
data = dataStr.split(" ")
#print(dataStr)
#print(data)
data = [int(value) for value in data]
#print(data)

for n in range(len(data)):
    if n % 2 == 0:
        print(data[n])