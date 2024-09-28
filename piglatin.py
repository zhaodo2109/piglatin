import string
import argparse

def pig_rule(word): # Define translation rules for text
    vowels = 'aeiou'
    capitalized = word[0].isupper() # Boolean function to check if the first index is Uppercase.
    if len(word) >= 2: #If string has more than 2 index
        char1 = word[0].lower() #Make first index lowercase
        char2 = word[1].lower() #Make second index lowercase
        if (char1 not in vowels) and (char2 in vowels): # Translate word starts with a consonant following up with a vowel
            word = word[1:] + word[0] + 'ay'
        elif (char1 not in vowels) and (char2 not in vowels): # Translate word starts with consonant following up with a consonant
            word = word[2:] + word[:2] + 'ay'
        else:
            word += 'way' #If word starts with a vowel
    else:
        char = word[0].lower()
        if (char in vowels): #If word starts with a vowel
            word += 'way'

    if capitalized: #Capitalized new word
        word = word[0].upper() + word[1:].lower()
    return word
def translate_to_pig(text): #Handle non letter character
    translate = ''
    i = 0
    while i < len(text):
        char1 = text[i]
        if char1.isalpha():
            j = 0
            while i + j < len(text) and text[i + j].isalpha(): #Keep iterating until find a non-letter character to break into word
                j += 1
            word = text[i:i + j]
            translate += pig_rule(word) #Apply pig latin rule
            i += j
        else:
            translate += char1
            i += 1

    return translate



if __name__ == '__main__':

    #Create argument parser
    default_output_file = "out.txt"
    default_input_file = "data.txt"
    parser = argparse.ArgumentParser(prog="Pig Latin", description= " Pig Latin Translator")
    parser.add_argument("--input",default = default_input_file, help="input filename",type = str)
    parser.add_argument("--output",default = default_output_file, help="output filename")
    args = parser.parse_args()

    with open(args.input, 'r') as file:
        output = translate_to_pig(file.read())
    with open(args.output, 'w') as output_file:
        output_file.write(output)


    print('inputfile:', args.input)
    print('outputfile:', args.output)

