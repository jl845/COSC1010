#
# Jordyn Luna
# 09/16/2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# This program prompts the user to enter the amount they have budgeted for the month, enter their expenses, and tell them if they are over or under their budget.

# Initialize variables for budget and expenses.
budget = 0.0
expense = 0.0
total = 0.0
Amount = 0.0    # Difference between the user's budget and expenses.

# Get amount user has budgeted for a month.
budget = float(input('Enter amount budgeted for the month: '))

# Amount of an expense.
print('Enter amount of an expense or enter 0 to end.')
expense = float(input('Amount of expense: '))
total += expense    # Calculate total of expenses.

# Make sure it is not less than 0.
while expense < 0:
    print('Error: The expense cannot be a negative.')
    expense = float(input('Amount of expense: '))
    total += expense

# Continue processing as long as user does not enter 0.
while expense != 0:
    expense = float(input('Amount of expense: '))
    total += expense

# Calculate if user is over or under their budget.
Amount = budget - total

# Display whether user is over or under their budget.
if budget > total:
    print('You are under your budget by $', format(Amount, ',.2f'))
else:
    print('You are over your budget by $', format(abs(Amount), ',.2f'))    # Display Amount as positive.