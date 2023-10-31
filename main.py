def print_menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encode(original_pass):
    encoded_pass = ""
    for i in range(len(original_pass)):
        encoded_pass += str((int(original_pass[i]))+3)
    return encoded_pass

def decode(encoded_pass):
    original_pass = ""
    for i in range(len(encoded_pass)):
        original_pass += str((int(encoded_pass[i]))-3)
    return original_pass

if __name__ == "__main__":

    loop = True
    while loop:
        print_menu()
        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:
            original_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(original_pass)
            print("Your password has been encoded and stored!")
        elif user_choice == 2:
            original_pass = decode(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {original_pass}.')
        elif user_choice == 3:
            break


