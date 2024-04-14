password_storage = {}

def encode_password(password):
    encoded = "".join(str((int(digit) + 3) % 10) for digit in password)
    return encoded

def decode_password(encoded_password):
    decoded = "".join(str((int(digit) - 3) % 10) for digit in encoded_password)
    return decoded

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
            password_storage['password'] = password
        elif option == "2":
            if 'encoded' in password_storage:
                encoded_password = password_storage['encoded']
                password = password_storage['password']
                decoded_password = decode_password(encoded_password)
                print("The encoded password is {}, and the original password is {}.".format(encoded_password, password))
        elif option == "3":
            break

menu()
