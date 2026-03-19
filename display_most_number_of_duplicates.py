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
    counts = Counter(numbers)
    most_common_data = counts.most_common(1)[0]
    number, frequency = most_common_data
    if frequency > 1:
        print(f"\nThe number with the most duplicate is {numbers} (appeared {frequency} times).")
    else:
        print("\nNo duplicates found:")