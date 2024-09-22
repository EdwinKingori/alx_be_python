pattern_size = int(input("Enter the size of the pattern: "))
row = 0
while row < pattern_size:
    for i in range(row + 1):
        print("*", end="")
    print()
    pattern_size += 1
