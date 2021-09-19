#!/usr/bin/env python3

# Created by: Mr. Matthew Meech
# Created on: Sep 2021
# This program is a number guessing game

import constants


def main():
   

    # input
    number = int(input("Enter number 0-9: "))
    print ("")

    # process & output 
   
    if number > constants.RIGHT_ANSWER: 
        print("you guessed wrong!")
    if number < constants.RIGHT_ANSWER: 
        print("you guessed wrong!")
    if number == constants.RIGHT_ANSWER: 
        print("you guessed right!")
    print("\nDone.")


if __name__ == "__main__":
    main()
    