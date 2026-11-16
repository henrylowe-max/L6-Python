Value = int(input("enter an integer (0-99): "))
Operation = input("calculate additive or multiplicative persistence (a or m): ")
count = 0
while Value > 9:
    if Operation == "a":
        Value = (Value // 10) + (Value % 10)
    else:
        Value = (Value // 10) * (Value % 10)
    count += 1
print(f"the persistence is: {count}")
