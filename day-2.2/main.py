#!/usr/bin/env python3
import math
import re

INPUT_FILE = 'input.txt'


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]

    return lines


def get_cube_count(game):
    cube_count = {'game_id': None, 'red': [], 'green': [], 'blue': []}
    cube_count['game_id'] = int(re.search(r'\d+', game).group())
    for grabbed_cubes in re.finditer(r'\d+ (red|green|blue)', game):
        count, color = grabbed_cubes.group().split()
        cube_count[color].append(int(count))

    return cube_count


def get_power_of_cubes(cube_count):
    minimum_cubes_needed = {'red': None, 'green': None, 'blue': None}
    for k, _ in minimum_cubes_needed.items():
        minimum_cubes_needed[k] = max(cube_count[k])

    power = math.prod((v for _, v in minimum_cubes_needed.items()))
    return power


def main():
    lines = get_input()
    cube_counts = [get_cube_count(game) for game in lines]
    print(sum((get_power_of_cubes(cube_count) for cube_count in cube_counts)))


if __name__ == '__main__':
    main()
