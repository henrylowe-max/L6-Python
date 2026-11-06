from pathlib import Path
def createTxtFile(fn:str):
    try:
        outF = open(fn)
        outF.close()
    except Exception as e:
        print(f"Exception: \n {e}")

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

def prependToTxtFile(data:list[str], fn:str) -> None:
    try:
        f = open(fn,"r")
        temp = f.read()
        f.close()
                
        f = open(fn, "w")
        f.write(data)
                
        f.write(temp)
        f.close()
    except Exception as e:
        print(f"Error filename {fn} doesnt exist")
        print(f"Exception: \n {e}")

def removeLine(fn:str, lineNo:int, ):
    try:
        with open(fn,"r") as inF:
            lines = inF.readlines()
        with open(fn,"w") as inF:
            for line in lines:
                if line.rstrip("\n") != lineNo:
                    inF.write(line)
        inF.close()
                    
    except Exception as e:  
            print(f"Error filename {fn} doesn't exist")
            print(f"Exception: \n {e}")

THIS_ROOT = Path(__file__).resolve().parent

#FULL_PATH = THIS_ROOT / "DATA" / FN

                
#createTxtFile(FULL_PATH)

#data = [input(f"enter line {n} ") for n in range(1,5+1)]
#print(data)
#appendToTxtFile(data,FULL_PATH)

#print("done")

print("[S] set file name - use current path \n[C] create a new file \n[A] append (add onto the end) a line \n[P] prepend (add a line to the beginning) a line.\n[D] display the file with line numbers\n[X] remove a line (prompt for line number)\n[Q] Quit")
quit = False
FN = str(input(f"choose a filename for file"))
FULL_PATH = THIS_ROOT / "DATA" / FN
while quit == False:
    choice = str(input("Choose an option from the list: ")).upper()
    if choice == "C":
        createTxtFile(FULL_PATH)
    elif choice == "S":
        FN = str(input("enter new filename"))
    elif choice == "A":
        appendToTxtFile(input("enter data list to append"), FULL_PATH)
    elif choice == "P":
        prependToTxtFile(input("add a string list to prepend to the file"), FULL_PATH)
    elif choice == "D":
        showTxtFile(FULL_PATH)
    elif choice == "X":
        removeLine(FULL_PATH,int(input("enter line number to remove")))
    elif choice == "Q":
        quit = True