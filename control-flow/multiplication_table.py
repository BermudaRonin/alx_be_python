number = int(input("Enter a number to see its multiplication table:"))

for x in range(10):
    multiplicator = x + 1
    result = number * multiplicator
    print(str(number) + " * " + str(multiplicator) + " = " + str(result))
