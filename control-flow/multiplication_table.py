number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    z = number * y
    print(str(number) + " * " + str(y) + " = " + str(z))
