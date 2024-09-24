#
# Jordyn Luna
# 09/23/2024
# Kilometer Converter Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# This program converts kilometers to miles.

# Constants 
Conversion_Factor = 0.6214

# Local variables
miles = 0
km = 0

def main():
    # Input Kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles (kilometers)

# The show_miles function converts the parameter km from kilometers to miles and displays the result.
def show_miles (km):
    # Convert Kilometers to Miles
    miles = km * Conversion_Factor

    # Display result of calculations
    print(km, 'kilometers equals', format(miles, '.4f'), 'miles.')

# Call the main function.
main ()