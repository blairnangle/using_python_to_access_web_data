import re


def get_input():
    global filename
    filename = input("Enter the name of the file you wish to parse: ")
    hand = open(filename, 'r')
    global words
    words = hand.read()
    return words


get_input()


def regex_fn():
    global numbers
    numbers = re.findall('[0-9]+', words)  # Basic regex to extract sequential strings of numbers of any length
    return numbers

regex_fn()


def sum_nums():
    count = 0
    for number in numbers:

        integer = int(number)
        count += integer
    print("The sum of the numbers in", filename, "is", count)


sum_nums()
