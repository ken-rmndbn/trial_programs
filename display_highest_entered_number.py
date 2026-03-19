numbers = []
while True:
    user_input = input("Enter Number: ")
    try:
        value = float(user_input)
        numbers.append(value)
    except ValueError:
        break