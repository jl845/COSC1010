#
# Jordyn Luna
# 11/10/2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    # Get a string from the user
    user_string = input('Enter a sentence: ')

    # Translate the sentence to pig latin
    pig_latin_sentence = translation(user_string)

    # Print the sentence in Pig Latin
    print('Pig Latin translation: ', pig_latin_sentence)

# Take a word in the sentence and translate to pig latin    
def pig_latin(word):
    # Remove the first letter and place it at the end of the word and append 'ay'
    return word[1:] + word[0] + 'ay'

# Translate the sentence to pig latin
def translation(sentence):
    
    # Split the sentence into words
    words = sentence.split()

    # Create a list for the words
    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + 'ay'
        pig_latin_words.append(pig_latin_word.upper())

    pig_latin_sentence = ''
    for i in range(len(pig_latin_words)):
        if i != 0:
            pig_latin_sentence += ' '
        pig_latin_sentence += pig_latin_words[i]

    return pig_latin_sentence        

# Call the main function
main()