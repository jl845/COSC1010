#
# Jordyn Luna
# 10/24/2024
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    try:    
        # Open numbers.txt file for reading
        numbers_file = open('numbers.txt', 'r')
    
        # local varaibles
        total = 0
        numberOfLines = 0
        
        # Read the first line from the file
        line = numbers_file.readlines()
    
        # As long as an empty string is not returned from readline, continue processing
        for line in line:
            total += int(line)              # total of the numbers
            numberOfLines += 1              # the number of lines
        
        average = total / numberOfLines     # Average of the numbers

        # Close the file
        numbers_file.close()          
    except IOError:
        print('An error occured trying to open and read the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    else:
        # Display the average
        print(f'The average of the numbers on the file numbers.txt is: {average}')    

# Call the main function
main()