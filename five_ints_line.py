#!/usr/bin/env python3

# Created by: Sarah
# Created on: May, 3rd, 2022
# This program displays numbers from 1000 to 2000 using a for loop. If the
# number is divisible by 5, it starts a new line.


def main():
    # initialize
    counter = 0

    # displays the numbers from 1000-2000 & then displays to user.
    for counter in range(1000, 2001):
        if counter % 5 == 0 and counter != 1000:
            print("")
        print(counter, " ", end="")


if __name__ == "__main__":
    main()
