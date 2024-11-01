#
# Jordyn Luna
# 10/16/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
     # Local variables
    total = 0
    numberOfLines = 0

    # Open numbers.txt file for reading
    numbers_file = open('numbers.txt', 'r')

    # Read the first line from the file
    line = numbers_file.readlines()
    
    # Read all lines in the file, find the total, and find the average
    for line in line:
         number = int(line)
         total += number              # total of the numbers
         numberOfLines += 1              # the number of lines
         
    average = total / numberOfLines     # Average of the numbers

    # Close the file
    numbers_file.close()       

    # Display the average
    print(f'The average of the numbers on the file numbers.txt is: {average}')

# Call the main function
main()