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
    numbers.sort(reverse = True)
    print("Numbers from highest to lowest")
    print(numbers)
else:
    print("No numbers entered")