text = input("Enter any word with spaces at the beginning: ")
index = 0
while index < len(text) and text[index] == " ":
    index += 1
cleaned_text = text[index:]
print("Original: ", text)
print("Left Stripped: ", cleaned_text)