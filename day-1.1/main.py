#!/usr/bin/env python3
import re

INPUT_FILE = 'input.txt'

def get_input() -> list(str):
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [ line[:-1] for line in lines ]

    return lines


def get_first_and_last_number(string: str) -> tuple(int, int):
    first_num = int(re.search(r'\d{1}', string).group())
    last_num = int(re.search(r'\d{1}', string[::-1]).group())

    return (first_num, last_num)


def combine_number_pair(number_pair: tuple) -> int:
    return number_pair[0]*10 + number_pair[1]


def main() -> None:
    lines = get_input()
    pairs = [get_first_and_last_number(line) for line in lines]
    combined_numbers = [combine_number_pair(pair) for pair in pairs]
    sum_of_combined_numbers = sum(combined_numbers)
    print(sum_of_combined_numbers)


if __name__ == '__main__':
    main()
