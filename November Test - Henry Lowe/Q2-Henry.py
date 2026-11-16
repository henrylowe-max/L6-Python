Word1 = str(input("enter the first word: "))
Word2 = str(input("enter the second word: "))
Word2List = []
count = 0
CanBeFormed = False
for x in range(len(Word2)):
        Word2List += Word2[x]
for i in range(len(Word1)):
    for y in range(len(Word2)):
        if Word2List[y] == Word1[i]:
            count += 1
            Word2List[y] = ""        
if count >= len(Word1):
    CanBeFormed = True 
print(CanBeFormed)