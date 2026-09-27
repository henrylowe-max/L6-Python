toDoList = []
currentTask = 0
Quit = False
def questions():
    print("1. Add to List")
    print("2. Display Whole List")
    print("3. Check Next Task")
    print("4. Completed Current Task")
    print("5. Quit")
    

 
while Quit == False:   
    questions()
    
    answer = int(input("what would you like to do? "))
    
    if answer == 1:
        toDoList.append(input("What task do you need to do. "))
        print(toDoList)
    elif answer == 2:
        print("your to do list:")
        for task in range(len(toDoList)):
            print(toDoList[task])
    elif answer == 3:
        print(f"your current task is: {toDoList[currentTask]}")
    elif answer == 4:
        print(f"{toDoList[currentTask]} Completed!!")
        toDoList.pop(currentTask)
    elif answer == 5:
        print("Goodbye")
        Quit = True
    else:
        print("invalid syntax, try again")