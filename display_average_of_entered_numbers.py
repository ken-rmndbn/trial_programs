numbers = []
while True:
    user_input = input("Enter a number: ")
    try:
        value = float(user_input)
        numbers.append(value)
    except ValueError:
        print("Invalid input")
        break
if numbers:
    average = sum(numbers) / len(numbers)
    print("The average of all numbers: ", average)
else:
    print("No numbers were entered")