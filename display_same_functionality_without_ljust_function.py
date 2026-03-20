user_input = input("Enter your text: ")
try:
    target_width = int(input("Enter desired width using number: "))
except ValueError:
    print("Please enter a valid number")
    exit()