first_number =[1]
for i in range(1,11):
    numbers = [float(input(f"Enter number {i}: "))]
result = [first_number - number for number in numbers[2:10]]
print(result)