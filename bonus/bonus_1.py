table = []
number = input("Enter number: ")
if number == "":
    print("No number")
else:
    while number != "":
        chislo = int(number)
        table.append(chislo)
        number = input("Enter number: ")
    common = sum(table)
    value = len(table)
    average = common/value
    minimum = min(table)
    maximum = max(table)
    print(minimum)
    print(maximum)
    print(average)
