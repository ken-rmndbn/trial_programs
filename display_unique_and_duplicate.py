while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Invalid input")
        break
    unique_digits = set(user_input)
    if len(unique_digits) == len(user_input):
        print("Unique:")
    else:
        print("Duplicate")