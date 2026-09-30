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
    while True:
        try:
            value = int(f"enter integer between {minV} and {maxV}: ")
        except:
            print("enter an integer")
        else:
            if minV <= value and value <= maxV:
                 return value
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
#for n in range(len(revBin)-1,0-1,-1):
# n = len(array)-1
#while n >= 0:
#   : :

# - - - -  function defs end here - - - - -

def main():
    placeValues = None        # Q1b) assign placeValue the list genrated by pv() {1 mark}
    data = None               # Q2b) call readDenaryInt() to read an integer between 100 and 4095 {1 mark}
    revBinary =  None # Q3c) call denToRevBin(placeValue,data) to assign binary the reversed binary value

    # call showData(placeValues, revBinary) below this line {1 mark}
    
    #- - - - end of main

if __name__ == "__main__":
    main()
