text = input("Enter text: ")
prefix_to_remove = input("Enter Prefix: ")
if text.startswith(prefix_to_remove):
    result = text[len(prefix_to_remove):]
else:
    result = text
print(result)