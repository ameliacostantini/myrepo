def print_menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encode(user_password):
    new_pass = ""
    for i in range(len(user_password)):
        new_pass += str((int(user_password[i]))+3)
    return new_pass

if __name__ == "__main__":

    loop = True
    while loop:
        print_menu()
        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:
            user_password = input("Please enter your password to encode: ")
            user_password = encode(user_password)
            print("Your password has been encoded and stored!")
        elif user_choice == 2:
            #decode()
            pass
        elif user_choice == 3:
            break


