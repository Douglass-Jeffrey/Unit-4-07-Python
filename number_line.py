#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program prints out numbers in intervals of five numbers per line


def main():
    # This function  prints out numbers in intervals of five numbers per line
    # variable
    line_num = 0

    # process & output
    for set_num in range(1000, 2001):
        print(set_num, sep="", end=" ")
        if line_num % 5 == 4:
            print("")
        line_num = line_num + 1


if __name__ == "__main__":
    main()
