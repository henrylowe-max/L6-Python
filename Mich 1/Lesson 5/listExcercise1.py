
name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']
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
    print(f"the last 7 names are: {name_list[11::1]}")
    print(f"length is {len(number_list)}")
    print(sum(number_list))
    print(max(number_list))
    print(min(number_list))
    print(sum(number_list) / len(number_list))
    
getAges()
getNames()
main()