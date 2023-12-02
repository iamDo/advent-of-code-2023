#!/usr/bin/env python3
import re

INPUT_FILE = 'input.txt'
MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


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


def is_cube_count_possible(game):
    return (max(game['red']) <= MAX_RED_CUBES) \
        and (max(game['green']) <= MAX_GREEN_CUBES) \
        and (max(game['blue']) <= MAX_BLUE_CUBES)


def main():
    lines = get_input()
    cube_counts = [get_cube_count(game) for game in lines]
    possible_games = filter(is_cube_count_possible, cube_counts)
    sum_of_possible_game_ids = sum((game['game_id'] for game in possible_games))
    print(sum_of_possible_game_ids)


if __name__ == '__main__':
    main()
