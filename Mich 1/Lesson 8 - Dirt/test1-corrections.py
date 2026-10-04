"""
Mini-test1.py
Marks : 15 Time : 20
NAME: 

"""
"""
Q1a

    Complete the function pv() that fills and
        returns a 12-element array with the binary place values thus:
        index 0 : 1 (2^0)
        index 1 : 2 (2^1)
        index 2 : 4 (2^2)
        : : :
        index 11 : 2048 (2^11)

Q1b. Calll this function in main {1 Mark}
"""


def pv() -> list[int]:
    return[2**n for n in range(12)]
    """
    Q1a) return the list [1,2,4,...]  {2 marks}
    """
    pass 

"""
  Q2. Write a function readDenaryInt(minV:integer,maxV:integer )->integer:
       
       Assumption : minV < maxV and both parameters are integers

       The funciton must:
       * prompts the user to input an integer value between minV and maxV.
       * validate the user input ensuring it is a  valid integer between minV and maxV is entered
       * trap the users input until a valid integer is entered with appropriate error messages
       * return the valid integer enterred
       {3 marks}
   Q2b. Calll this function in main {1 Mark}
"""
def readDenaryInt(minV:int, maxV:int) -> int:
    ok = False
    while ok == False:
        try:
            value = int(input(f"enter integer between {minV} and {maxV}: "))
        except:
            print("enter an integer")
        else:
            if minV <= value and value <= maxV:
                return value
                ok = True
            else:
                print(f"enter integer between {minV} and {maxV}: ")


"""
  Q3. Write a function denToRevBin(placeValues:list,data:integer)->integer:
       that :
       * Generates "revBin" as a 12-element array  of integers with all entries set to zero

       Impelemts the following ALGORITHM:
        LOOP over placeValues in REVERSE ORDER (i.e. 4096,...,4,2,1):
                set revBin[x] to data DIV placeValue[x]
                set data to data MOD placeValue[x]

            return revBin
      
       {3 marks}
    Q3b. Calll this function in main {1 Mark}
"""
def denToRevBin(placeValues:list,data:int)-> list:
    revBin = [ 0 for _ in range(len(placeValues))]

    for n in range(len(revBin)-1,0-1,-1):
        revBin[n] = data  //  placeValues[n]
        data = data % placeValues[n]
        
    return revBin

def showData(placeValues, revBinary):
    
    s = ""
    for n in range(len(revBinary)):
        s += (f"{placeValues[n]:5}")
    print(s)
    for n in range(len(revBinary)):
        s += (f"{revBinary[n]:5}")
    print(s)
    
    pv = placeValues[:]
    pv.reverse()
        
    revBinary = revBinary[:]
    revBinary.reverse()
    
    return
    

    
    
    pv = placeValues[:]
    pv.reverse()
    
    revBinary = revBinary[:]
    revBinary.reverse()
    






## q4 


def hexConv(revBinary):
    hexValues = "0123456789ABCDEF"
    nibbles = [revBinary[i:i+4] for i in range(0, len(revBinary), 4)]
    hexa = ""
    
    for nibble in nibbles:
        nibble = nibble[::-1]
        denary = 0
        for digit in nibble:
            denary = denary * 2 + digit
        
        hexa = hexValues[denary] + hexa
    return hexa
    
    
        
    
    #print(nib1)
    #print(nib2)
    #print(nib3)
    
#- - - -  function defs end here - - - - -

def main():
    placeValues = pv()      # Q1b) assign placeValue the list genrated by pv() {1 mark}
    data = readDenaryInt(100,4095)               # Q2b) call readDenaryInt() to read an integer between 100 and 4095 {1 mark}
    revBinary = denToRevBin(placeValues,data)   # Q3c) call denToRevBin(placeValue,data) to assign binary the reversed binary value

    # call showData(placeValues, revBinary) below this line {1 mark}
    showData(placeValues, revBinary)
    
    print(placeValues)
    print(revBinary)
    Hex = hexConv(revBinary)
    print(Hex)
    
    
    
    #- - - - end of main

if __name__ == "__main__":
    main()
