user_input = input("Enter Text: ")
result = " ".join([word[0].upper() + word[1:].lower() for word in user_input.split()])
print("First letter text capitalization: ", result)