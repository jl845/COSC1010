#
# Jordyn Luna
# 10/16/2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Declare local variables
    contents = ''

    # Open numbers.txt file for reading
    infile = open('numbers.txt', 'r')

    # Read in data and store in content
    contents = infile.read()

    # Close file
    infile.close()

    # Print contents
    print(contents)

# Call the main function
main()    