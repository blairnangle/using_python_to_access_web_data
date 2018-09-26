import re


def get_input():
    global filename
    filename = raw_input("Enter the name of the file you wish to parse: ")
    hand = open(filename, 'r')
    global words
    words = hand.read()
    print words


get_input()


def regex_fn():
    my_list = []
    for line in words.splitlines():
        numbers = re.findall('\d+.\d+', line)
        my_list.append(numbers[1])
    my_list = sorted(my_list, reverse=True)
    print my_list

regex_fn()

# Program to extract numbers from a file and sort in descending order
