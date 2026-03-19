duplicates = []
numbers = [float(input(f"Enter number {i}: ")) for i in range (1, 11)]
for duplicate in numbers:
    if numbers.count(duplicate) > 1 and duplicate not in duplicates:
        duplicates.append(duplicate)
print("Duplicates: ", duplicates)