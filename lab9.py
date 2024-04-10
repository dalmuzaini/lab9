password_storage = {}

def encode_password(password):
    encoded = "".join(str((int(digit) + 3) % 10) for digit in password)
    return encoded

def menu():
    while True:
        print("\nMenu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
            password_storage['encoded'] = encoded_password
        elif option == "3":
            break

menu()