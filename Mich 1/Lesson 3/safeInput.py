def safeIntInput(prompt:str) -> int:
    ok = False
    while not ok:
        try:
            data = int(input(prompt))
        except:
            print("Please enter an integer")
        else:
            ok = True
    return data

def main():
    age = safeIntInput("enter your age")
    print(f"age is of type {type(age)}")
    if isinstance(age,int):
        print("age is an integer")
    
if __name__ == "__main__":
    main()