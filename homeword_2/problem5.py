def calc_num_vowels(string):
    vowels = 'aeiou'
    num_vowels = 0
    for ch in string:
        if ch.lower() in vowels:
            num_vowels += 1
    return num_vowels

def calc_num_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    num_consonants = 0
    for ch in string:
        if ch.lower() in consonants:
            num_consonants += 1
    return num_consonants

users_string = input('Enter a string of characters: ')

vowels = calc_num_vowels(users_string)
consonants = calc_num_consonants(users_string)

print('Your string has', vowels, 'vowels and', consonants, 'consonants.')
