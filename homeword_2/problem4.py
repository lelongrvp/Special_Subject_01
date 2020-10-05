def to_sentence_case(string):
    ending_punctuation = []
    for i in range(len(string)):
        if string[i] == '.':
            ending_punctuation.append('.')
        elif string[i] == '?':
            ending_punctuation.append('?')
        elif string[i] == '!':
            ending_punctuation.append('!')
    
    string = string.replace('?', '.').replace('!', '.')
    sentences = string.split('.')
    while '' in sentences:
        sentences.remove('')
    
    ind = []
    for i in range(len(sentences)):
        sentences[i] = sentences[i].lstrip(' ')
        sentences[i] = sentences[i][0].upper() + sentences[i][1:]
            
    new_string = ''
    for i in range(len(sentences)):
        new_string += sentences[i]
        new_string += ending_punctuation[i] + ' '
    new_string = new_string[:-1]
        
    return new_string
    return sentences

users_string = input('Enter a few sentences in all lowercase: ')
print('\nIn sentence case, your sentences look like')
print(to_sentence_case(users_string))