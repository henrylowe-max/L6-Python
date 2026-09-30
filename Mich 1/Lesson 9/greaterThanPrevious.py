#Given a list of numbers, find and print all the elements that are greater than the previous element.
#input = 1 5 2 4 3

dataStr = input("")
data = dataStr.split(" ")

for n in range(len(data)0,:,1):
    if data[n] > data[n-1]:
        print(data[n])
