from safeFloatinput import *
Max = 5
names = [str() for n in range(Max)]
ages = [str() for i in range(Max)]

def getNames() -> list[str]:
    for n in range(Max):
        names[n] = str(input(f"enter name {n+1} "))
    return names

def getAges() -> list[int]:
    for i in range(Max):
        ages[n] = str(input(f"enter age {i+1} "))
    return ages

def getInfo() -> None:
    for x in range(len(ages)):
        print(f"{names[n]:15} {ages[i]:5}")
        
def main():
    names = getNames()
    ages = getAges()
    info = getInfo()
    print(names)
    print(ages)
    print(info)
    
if __name__ == "__main__":
    main()