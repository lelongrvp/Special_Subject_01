# Ask user to enter the full name
full_name = input('Enter your full name: ')

error = True
while error == True:
    try:
        # Split the name into 3 parts: first name, middle name and last name.
        first, middle, last = full_name.split()
        error = False
    except ValueError:
        # Print the error message if the input does not follow the requirement
        print('\nError: This program only works if you have exactly three names. Try again!')
        # Ask the user to enter again.
        full_name = input('Enter your full name: ')

# Print the initials of the name, with the first letter of each name
print('\nYour initials are', first[0].upper() + '.', middle[0].upper() + '.', last[0].upper() + '.')