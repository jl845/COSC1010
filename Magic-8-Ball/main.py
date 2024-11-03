#
# Jordyn Luna
# 10/30/2024
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random
def main():
    try:
        # Open file to read
        infile = open('8_ball_responses.txt', 'r')

        # Read contents of file into a list
        responses = infile.readlines()

        # Close file
        infile.close()

        responses = [response.strip() for response in responses]

        print('Welcome to the Magic 8 Ball.')

        # Create a variable
        keep_going = 'yes'
    
        while keep_going == 'yes':

            question = input('Ask a yes or no question, or type quit to exit: ')

            if question.lower() == 'quit':
                print('Thanks for playing!')
                break
            else:
                response = random.choice(responses)
                print(f'Magic 8 Ball says: {response}')
    except FileNotFoundError:
        print("Error: The file '8_ball_responses.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")        

# Call the main function
main()
