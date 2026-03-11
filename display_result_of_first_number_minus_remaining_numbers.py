numbers = []
for i in range(1,11):
    value = float(input(f"Enter number {i}: "))
    numbers.append(value)
first_number = numbers[0]
result = [first_number - number for number in numbers[1:]]
print("First number minus the remaining number = ", result)