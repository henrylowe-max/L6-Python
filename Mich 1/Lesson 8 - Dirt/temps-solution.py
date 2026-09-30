#,
#Write a well designed python program that:
#Prompts the user to enter F or C for an input temperature’s unit
#Prompt the user to enter the temperature
#Report the temperature in the alternate units
#* Your code should validate and trap input units to only be F or C
#* Your code should use functions / procedures
#* Your program should produce well formatted outputs 
#Extension: Include K as a unit.

#C = (F-32)*(5/9)
#F = C*(9/5) + 32

#lookup:
#K = C + 273.15
#so
#C = K - 273.15


def getUnits():
    units = ""
    validUnits = "CFK"
    while units not in validUnits:
        units = str(input(f"Enter units {validUnits}"))
        units = units.upper()
    return units

def getTemp(units):
    temp = float(input(f"enter temp in {units}"))
    return temp

units = getUnits()
temp = getTemp(units)

def F_to_C(temp):
    return (temp-32)*(5/9)

def C_to_F(temp):
    return (temp)*(9/5) + 32

def K_to_C(temp):
    return temp + 273.15

def C_to_K(temp):
    return temp - 273.15


if units == "F":
    print(f"{temp} F = {F_to_C(temp):.2f}")
    print(f"{temp} F = {F_to_C(C_to_K(temp)):.2f}")
elif units == "C":
    print(f"{temp} C = {C_to_F(temp):.2f}")
    print(f"{temp} C = {C_to_K(temp):.2f}")
elif units == "K":
    print(f"{temp} K = {K_to_C(temp):.2f}")
    print(f"{temp} K = {K_to_C(C_to_K(temp)):.2f}")
    

    

    
#print(f"temperature = {temp} {units}")
