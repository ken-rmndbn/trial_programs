def find_lowest_number():
    lowest = float("inf")
    count = 0
    while True:
        user_input = input("Enter a number: ")
        try:
            number = float(user_input)
            if number < lowest:
                lowest = number
            count += 1

