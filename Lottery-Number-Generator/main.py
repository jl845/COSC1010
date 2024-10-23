#
# Jordyn Luna
# 10/23/2024
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Constants
Max_Digits = 7  # Max number of digits
Start = 0       # Start of the random number range
End = 9         # End of the random number range

import random

# Main function
def main():
    # Create a list
    numbers = [0] * 7

    # Create the list with random numbers
    for index in range (Max_Digits):
        numbers[index] = random.randint(Start, End)

    # Display the random numbers
    print('Here are your lottery numbers:')
    for index in range (Max_Digits):
        print(numbers[index], end='')
    print()

# Call the main function
main()         
