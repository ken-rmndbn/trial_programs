user_input = input("Enter your text: ")
try:
    target_width = int(input("Enter desired width using number: "))
except ValueError:
    print("Please enter a valid number")
    exit()
space_to_add = target_width - len(user_input)
final_string = user_input + (" " * space_to_add)
print("Original Length: ", len(user_input))
print("Result: ", final_string)
print("New Length: ", len(final_string))