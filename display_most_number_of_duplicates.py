from collections import Counter
numbers = []
while True:
    user_input = input("Enter Number: ")
    try:
        value = float(user_input)
        numbers.append(value)
    except ValueError:
        break
if numbers:
    most_duplicate = max(set(numbers), key = numbers.count)
    if numbers.count(most_duplicate) > 1:
        print(f"The most duplicate number is: {most_duplicate}")
    else:
        print("No duplicates")