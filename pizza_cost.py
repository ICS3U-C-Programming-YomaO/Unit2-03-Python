#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: September 30, 2025
# This program calculates pizza cost with user input


import constants

def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax
    #output
    print("")
    print("The total cost is = ${:,.2f}".format(total))

if __name__ == "__main__":
    main()


