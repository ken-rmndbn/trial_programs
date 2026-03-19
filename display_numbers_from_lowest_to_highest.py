numbers = []
while True:
    user_input = input("Enter a number: ")
    try:
        value = float(user_input)
        numbers.append(value)
    except ValueError:
        print("Invalid Input")
        break
if numbers:
    numbers.sort()
    print("Numbers from lowest to highest")
    print(numbers)
else:
    print("No numbers entered")