#
# Jordyn Luna
# 09/26/2024
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.

# Local Variables
feet = 0

# Constants 
Inches_Per_Foot = 12

# main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches
def feet_to_inches (feet): 
    return feet * Inches_Per_Foot

# Call the main function
main()

