# Victer Qiu

def encode(string):
	encoded_string = []
	for i in string:
		x = int(i) + 3
		if x > 9: # we take the ones digit
			x %= 10
		encoded_string.append(str(x))# add x as a string to the list
	return ''.join(encoded_string) # joinds the list into a string

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
	elif option == 2:
		print(f'The encoded password is {encode(password)}, and the original password is {password}.')
	else:
		break


