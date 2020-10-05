users_string = input('Enter a string of characters: ')

num_characters = [0]*256
for ch in users_string:
    num_characters[ord(ch)] += 1

most_frequent = chr(num_characters.index(max(num_characters)))

if most_frequent == ' ':
    most_frequent = 'the space character'

print ('\nThe most frequent character in your string is', most_fre quent.lower() + '.')