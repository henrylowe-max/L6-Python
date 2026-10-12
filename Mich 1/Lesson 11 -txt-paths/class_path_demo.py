from pathlib import Path

# windows \
# mac or linux /

#get parent directory

THIS_ROOT = Path(__file__).resolve().parent

FN = "numbers.txt"

FULL_PATH = THIS_ROOT / "DATA" / FN

print(FULL_PATH)

"""
Write the numbers 1 - 15 to the text 
file "numbers.txt"

save in this current file
"""
def createTxtFile(fn:str):
    outF = open(FULL_PATH, "w")
    for i in range(1,16):
        outF.write(f"{i}\n")

    outF.close()

def showTxtFile(fn:str) -> None:
    lineNo = 0 #increment at start of loop
    try:
        with open(fn,"r") as inF:
            for aLine in inF:
                lineNo += 1
                aLine = aLine.rstrip("\n")
                print(f"{lineNo :02d} : {aLine}")
    except Exception as e:  
        print(f"Error filename {fn} doesn't exist")
        print(f"Exception: \n {e}")

def appendToTxtFile(data:list[str], fn:str) -> None:
    lineNo = 0 #increment at start of loop
    try:
        with open(fn,"a") as outF:
            for aLine in data:
                outF.write(f"{aLine}\n")
        
        print("data added to file")
                
    except Exception as e:  
        print(f"Error filename {fn} doesn't exist")
        print(f"Exception: \n {e}")
                
createTxtFile(FULL_PATH)
appendToTxtFile(FULL_PATH)

data = [input(f"enter line {n} ") for n in range(1,5+1)]
print(data)
appendToTxtFile(data,FULL_PATH)

print("done")