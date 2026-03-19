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
        except ValueError:
            print("Invalid input")
            break
    if count > 0:
        print("The lowest number you entered was: ", lowest)
    else:
        print("No valid numbers entered")
if __name__ == "__main__":
    find_lowest_number()
