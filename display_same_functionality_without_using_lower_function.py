text = input("Enter any word or text: ")
result = ""
for character in text:
    if "A" <= character <= "Z":
        lower_character = chr(ord(character) + 32)
        result += lower_character
    else:
        result += character
print("Original: ", text)
print("Lowercase: ", result)