numbers = []
while True:
    user_input = input("Enter Number: ")
    try:
        value = float(user_input)
        numbers.append(value)
    except ValueError:
        break
if numbers:
    highest_number = max(numbers)
    print("The highest number you entered is:", highest_number)
else:
    print("Invalid input")