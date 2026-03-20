def manual_center(text, width):
    total_padding = width - len(text)
    if total_padding <= 0:
        return text
    left_side = total_padding // 2
    right_side = total_padding - left_side
    return (" " * left_side) + text + (" " * right_side)
user_text = input("Enter Text: ")
try:
    user_width = int(input("Enter total width in number: "))
    centered_result = manual_center(user_text, user_width)
    print("Result:", centered_result)
    print("Total length: ", len(centered_result), "characters")
except ValueError:
    print("Error! Please enter valid number for width")