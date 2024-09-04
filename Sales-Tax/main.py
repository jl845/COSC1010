#
# Jordyn Luna
# 09/04/2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates

# Get the amount of the purchase.
amount_of_purchase = float(input('Enter the amount of the purchase: '))
# Calculate the state sales tax.
state_sales_tax = amount_of_purchase * 0.05
# Calculate the county sales tax.
county_sales_tax = amount_of_purchase * 0.025
# Calculate the total tax.
total_tax = state_sales_tax + county_sales_tax
# Calculate the total of the sale.
TotalOfTheSale = amount_of_purchase + total_tax
# Print information about the sale.
print('The total is $', format(TotalOfTheSale, ',.2f'))