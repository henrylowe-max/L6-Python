def safeFloatInput(prompt:float) -> float:
    ok = False
    while not ok:
        try:
            data = float(input(prompt))
        except:
            print("Please enter a float")
        else:
            ok = True
    return data

def main():
    age = safeFloatInput("enter your age")
    print(f"age is of type {type(age)}")
    if isinstance(age,float):
        print("age is a float")
    else:
        print("age is not a float")
        
if __name__ == "__main__":
    main()