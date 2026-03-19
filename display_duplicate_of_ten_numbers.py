duplicates = []
numbers = [float(input(f"Enter number {i}: ")) for i in range (1, 11)]
for x in numbers:
    if numbers.count(x) > 1 and x is not in duplicates:
        duplicates.append(x)
print("Duplicates: ", duplicates)