#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2-21
# This program creates a 2 array of random numbers and calculates their average

import random


def average_of_numbers(passed_in_2D_list):
    # this function calculates the average of
    #   all the elements in  a 2D array

    total = 0

    for row_value in passed_in_2D_list:
        for single_element in row_value:
            # total = total + single_element
            total += single_element

    average = total / (len(row_value) * len(passed_in_2D_list))

    return average


def main():
    # gets input, outputs array

    a_2d_list = []

    # input
    rows_as_string = input("How many row would you like: ")
    columns_as_string = input("How many columns would you like: ")
    print("")

    try:
        # string to integer
        rows_as_number = int(rows_as_string)
        columns_as_number = int(columns_as_string)

        # generate random numbers and insert them into array
        if rows_as_number > 0 & columns_as_number:
            for loop_counter_rows in range(0, rows_as_number):
                temp_column = []
                for loop_counter_columns in range(0, columns_as_number):
                    a_random_number = random.randint(1, 50)
                    temp_column.append(a_random_number)
                    print("{0} ".format(a_random_number), end="")
                a_2d_list.append(temp_column)
                print("\n")

            # outputs average
            final_output = average_of_numbers(a_2d_list)
            print("The average of all the numbers: {0} ".format(final_output))
        else:
            print("Number of columns and rows must be positive")

    except Exception:
        print("Invalid number of rows or columns")


if __name__ == "__main__":
    main()
