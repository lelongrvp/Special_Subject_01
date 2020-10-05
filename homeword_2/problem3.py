# Obtain phone number from user and split it into 3 parts
phone_number = input('Enter a phone number using the format XXX-XXX-XXXX: ')
split_number = phone_number.split('-')

#initializing some control variables
weird_character = False # True will stop while loop and display an error

count = 0       # Keeps track of which part of phone number we're 
                # currently looking at: area code, central office
                # prefix, or line number

# This will hold the numeric version of the user's phone number
numeric_phone_number = ''

# Loop over each of the 3 parts of the number and over each character in that part.
while weird_character == False and count < 3:
    for ch in split_number[count]:
        if ch.isdigit():
            numeric_phone_number += ch
        elif ch.upper() in 'ABC':
            numeric_phone_number += '2'
        elif ch.upper() in 'DEF':
            numeric_phone_number += '3'
        elif ch.upper() in 'GHI':
            numeric_phone_number += '4'
        elif ch.upper() in 'JKL':
            numeric_phone_number += '5'
        elif ch.upper() in 'MNO':
            numeric_phone_number += '6'
        elif ch.upper() in 'PQRS':
            numeric_phone_number += '7'
        elif ch.upper() in 'TUV':
            numeric_phone_number += '8'
        elif ch.upper() in 'WXYZ':
            numeric_phone_number += '9'
        else:
            weird_character = True
    if count != 2:
        numeric_phone_number += '-'
    count += 1

# Error message if non-alphanumeric character pops up
if weird_character:
    print('\nSome weird characters showed up in the number that I don\'t know what to do with.')

# Otherwise, here's some numeric version of the phone number
else:
    print ('\nThe phone number you entered is', numeric_phone_number + '.')