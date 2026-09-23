name_list: list[str] = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']
number_list = []
def getNames():
    for i in range(3):
        name = input("Type in a name: ")
        name_list.append(name)
    
def getAges():
    for i in range(5):
        number = int(input(f"enter number {i+1}: "))
        number_list.append(number)
    
def main():
    print(name_list)
    print(f"the third name is: {name_list[2]}")
    print(f"the last 7 names are: {name_list[(len(name_list) - 7):]}")
    print(f"length is {len(number_list)}")
    print(f"sum is{sum(number_list)}")
    print(number_list[-1])
    print(number_list[0])
    print(sum(number_list) / len(number_list))
    
getAges()
getNames()
main()