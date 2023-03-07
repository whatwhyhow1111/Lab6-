
def encode_password(password):
    encode = ""
    for char in password:
        new_char = int(char) + 3
        encode += str(new_char)
    return encode

def decode_password(encode):
    pass

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 3:
            break
        if option == 1:
            password = input("Please enter your password to encode: ")
            encode = encode_password(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            decode = decode_password(encode)
            print("The encoded password is "+encode+", the original password is "+decode+".")

if __name__ == "__main__":
    main()