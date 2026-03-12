numbers = [float(input(f"Enter number {i}: ")) for i in range (1, 11)]
even_numbers = [number for number in numbers if number % 2 == 0]
count_even_numbers = len(even_numbers)
print("There are", count_even_numbers, "even numbers")
