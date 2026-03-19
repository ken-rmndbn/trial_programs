numbers = []
while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid Input")
        break
        