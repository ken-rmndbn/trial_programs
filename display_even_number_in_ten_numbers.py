numbers = [float(input(f"Enter number {i}: ")) for i in range (1, 11)]
odd_numbers = [number for number in numbers if number % 2 == 0]
