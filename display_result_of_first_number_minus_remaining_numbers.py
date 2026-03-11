numbers = []
for i in range(1,11):
    value = float(input(f"Enter number {i}: "))
    numbers.append(value)
first_number = numbers[0]
for number in numbers[1:]:
    first_number -= number
print("First number minus the remaining number = ", first_number)