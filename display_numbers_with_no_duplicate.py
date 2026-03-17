numbers = [float(input(f"Enter number {i}: ")) for i in range (1, 11)]
unique_number = [number for number in numbers if numbers.count(number) == 1]
print("Numbers with no duplicates: ", unique_number if unique_number else "None")