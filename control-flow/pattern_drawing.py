size = int(input("Enter the size of the pattern: "))

current = 1

while current <= size:
    for i in range(1, size + 1):
        print("*", end="")
    print()
    current = current + 1
