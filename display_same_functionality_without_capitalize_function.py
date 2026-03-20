user_input = input("Enter text: ")
result = user_input[0].upper() + user_input[1:].lower() if user_input else ""
print("Fixed Capitalization: ", result)