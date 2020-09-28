#Python program to implement Morse Code Translator

#Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':".-", 'B':'-...', 'C':'-.-.',
                     'D':'-..', 'E':'.', 'F':'..-.', 
                     'G':'--.', 'H':'....', 'I':'..', 
                     'J':'.---', 'K':'-.-', 'L':'.-..', 
                     'M':'--', 'N':'-.', 'O':'---', 
                     'P':'.--.', 'Q':'--.-', 'R':'.-.', 
                     'S':'...', 'T':'-', 'U':'..-', 
                     'V':'...-', 'W':'.--', 'X':'-..-', 
                     'Y':'-.-', 'Z':'--..', '0':'-----',
                     '1':'.----', '2':'..---', '3':'...--',
                     '4':'....-', '5':'.....', '6':'-....',
                     '7':'--...', '8':'---..', '9':'----.',
                     ' ':' ', ',':'--.--', '.':'.-.-.-', '?':'..--..'}

userInput = input("Enter your string: ")
for character in userInput:
    character = character.upper()
    print(MORSE_CODE_DICT[character], end = '')
