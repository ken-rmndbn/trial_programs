numbers = [float(input(f"Enter number {i}: ")) for i in range (1, 11)]
unique_ordered = list(dict.fromkeys(numbers))
print("Duplicates removed, first entry kept: ", unique_ordered)