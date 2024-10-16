#
# Jordyn Luna
# 10/16/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Declare local variables
    contents = ''

    # Open numbers.txt file for reading
    infile = open('numbers.txt', 'r')

    # Read numbers in the file
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Close the file
    infile.close()

    # Add the three numbers
    total = num1 + num2 + num3

    # Find the average of the three numbers
    average = total / 3

    # Display the average
    print(f'The average of the numbers on the file numbers.txt is: {average}')

# Call the main function
main()