number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
if number_1 < number_2:
    starting_number = number_1 + 1
    while starting_number < number_2:
        print(starting_number)
        starting_number += 1
else:
    starting_number = number_1 - 1
    while starting_number > number_2:
        print(starting_number)
        starting_number -= 1