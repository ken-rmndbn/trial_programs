def is_it_uppercase(text):
    if text == text.upper() and text.lower() != text.upper():
        return True
    else:
        return False
user_input = input("Enter a text: ")
if is_it_uppercase(user_input):
    print("This is strictly UPPERCASE")
else:
    print("No, it contains lowercase letter  or no letter at all")