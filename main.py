# Victer Qiu

def encode(string):
    encoded_string = []
    for i in string:
        x = int(i) + 3
        if x > 9:  # we take the ones digit
            x %= 10
        encoded_string.append(str(x))  # add x to the list
    encoded_pass = ''.join(encoded_string)  # joinds the list into a string
    return encoded_pass


def decode():
    pass
    return decoded_pass


if __name__ == '__main__':
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
			encoded_password = encode(password)
        elif option == 2:
			decoded_passwor = decode(password)
            print(f'The encoded password is {encode_password}, and the original password is {decoded_password}.')
        else:
            break
