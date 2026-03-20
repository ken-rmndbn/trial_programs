def main():
    user_input = input("Enter text you want to swap: ")
    swapped = "".join([
        character.lower() if character.isupper() else character.upper()
        for character in user_input
    ])
    print("Result: ", swapped)
if __name__ == "__main__":
    main()