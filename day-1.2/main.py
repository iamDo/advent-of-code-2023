#!/usr/bin/env python3
import re

INPUT_FILE = 'input.txt'
NUMBER_DICTIONARY = {
    'zero':  0,
    'one':   1,
    'two':   2,
    'three': 3,
    'four':  4,
    'five':  5,
    'six':   6,
    'seven': 7,
    'eight': 8,
    'nine':  9,
}
NUMBER_REGEX = r'{}'.format('|'.join(NUMBER_DICTIONARY.keys()))


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [ line[:-1] for line in lines ]

    return lines


def get_numbers_and_digits(string:str):
    number_or_digit_regex = ''.join(['(?=(', NUMBER_REGEX, '|\d)){1}'])
    return re.findall(number_or_digit_regex, string)


def ensure_digit(number_or_digit: str):
    digit = None
    if number_or_digit.isdigit():
        digit = int(number_or_digit)
    else:
        digit = NUMBER_DICTIONARY[number_or_digit]
    return digit


def get_pair(string: str):
    numbers_and_digits = get_numbers_and_digits(string)
    first_member = ensure_digit(numbers_and_digits[0])
    second_member = ensure_digit(numbers_and_digits[-1])
    return (first_member, second_member)


def combine_number_pair(number_pair: tuple):
    return number_pair[0]*10 + number_pair[1]


def main():
    lines = get_input()
    pairs = [ get_pair(line) for line in lines ]
    combined_numbers = [ combine_number_pair(pair) for pair in pairs ]
    sum_of_combined_numbers = sum(combined_numbers)
    print(sum_of_combined_numbers)


if __name__ == '__main__':
    main()
