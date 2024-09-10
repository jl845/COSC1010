#
# Jordyn Luna
# 09/09/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Constants
hotDogsPerPackage = 10
bunsPerPackage = 8

# Local variables
numberOfPeople = 0      # The number of people attending
hotDogsPerPerson = 0    # The number of hot dogs per person
total_hot_dogs = 0      # The total number of hot dogs and buns needed
minDogs = 0             # The minimum number of packages of hot dogs
minBuns = 0             # The minimum number of packages of hot dog buns
dogsLeft = 0            # The number of hot dogs left over from a package
bunsLeft = 0            # The number of hot dog buns left over from a package

# Get the number of people attending the cookout.
numberOfPeople = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs each person will be given.
hotDogsPerPerson = int(input('Enter the number of hot dogs per person: '))

# Calculate the total number of hot dogs.
total_hot_dogs = numberOfPeople * hotDogsPerPerson

# Calculate the number of hot dog packages required.
minDogs = total_hot_dogs // hotDogsPerPackage

# Calculate the number of hot dog bun packages required.
minBuns = total_hot_dogs // bunsPerPackage

# Determine if the number of people attending is large enough to require more than one package of hot dogs.
if minDogs > 0: 
    # Calculate the number of hot dogs left over from a package, if any.
    dogsLeft = total_hot_dogs % hotDogsPerPackage

    # If there will be left overs, add an additional package of hot dogs.
    if dogsLeft != 0:
        minDogs += 1
# Set the minimum number of packages of hot dogs to one because the number of people attending is small enough to require only one package of hot dogs.
else:
    minDogs =  1

# Determine the number of leftover hot dogs, if any.
dogsLeft = (hotDogsPerPackage * minDogs) - total_hot_dogs

# Determine if the number of people attending is large enough to require more than one package of hot dog buns.
if minBuns > 0:
    # Calculate the number of hot dog buns left over from a package, if any.
    bunsLeft = total_hot_dogs % bunsPerPackage

    # If there will be left overs, add an additional package of hot dog buns.
    if bunsLeft != 0:
        minBuns += 1
# Set the minimum number of packages of hot dogs to one because the number of people attending is small enough to require only one package of hot dog buns.
else:
    minBuns = 1

# Determine the number of leftover hot dog buns, if any.
bunsLeft = (bunsPerPackage * minBuns) - total_hot_dogs

# Display the minimum packages of hot dogs needed.
print('Minimum packages of hot dogs needed: ', minDogs)

# Display the minimum packages of hot dog buns needed.
print('Minimum packages of hot dog buns needed: ', minBuns)

# Display the number of hot dogs left over.
print('Hot dogs left over: ', dogsLeft)

# Display the number of hot dog buns left over.
print('Hot dog buns left over: ', bunsLeft)