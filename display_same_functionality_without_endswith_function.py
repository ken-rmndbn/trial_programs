text_input = input("Enter text: ")
suffix_input = input("Enter suffix of ending: ")
if len(suffix_input) <= len(text_input) and text_input[-len(suffix_input):] == suffix_input:
    print("Right!", text_input, "ends with", suffix_input)
else:
    print("No,", text_input, "does not end with", suffix_input)