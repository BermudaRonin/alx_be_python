number = int(input("Enter a number to see its multiplication table:"))

for x in range(1, 11):
    print(str(number) + " * " + str(x) + " = " + str(number * x))
