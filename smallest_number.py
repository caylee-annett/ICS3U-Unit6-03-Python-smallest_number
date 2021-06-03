#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This program finds the smallest number from a list of random numbers and uses
#   a For In loop

import random


def calculate_number(list_of_numbers):
    # This function finds the smallest number

    smallest_number = 100

    for counter in list_of_numbers:
        if counter <= smallest_number:
            smallest_number = counter

    return smallest_number


def main():
    # This function generates the random numbers

    number_list = []

    # Process
    print("This program prints the smallest number from a list.")
    print("")
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        print("The random number is: {}".format(random_number))
        number_list.append(random_number)

    # Call functions
    number = calculate_number(number_list)

    # Output
    print("")
    print("The smallest number is: {}".format(number))
    print("\nDone.")


if __name__ == "__main__":
    main()
