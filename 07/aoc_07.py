""" AOC 2025 day 7 """

import numpy as np
from collections import defaultdict
import time
import re

def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def input_reader2(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]

def run_part1(input_file):
    inp = input_reader2(input_file)
    mapping = {'.': 0, '^': 1, 'S': 3}
    grid = np.asarray([[mapping[i] for i in n] for n in inp]).astype(int)
    validate_grid = np.copy(grid)
    start_pos = [p[0] for p in np.where(grid == 3)]
    beam_positions = [start_pos[1]]
    total = 0
    for row in range(grid.shape[0]-1):
        tmp_pos = []
        for pos in beam_positions:
            if grid[row+1, pos] == 1:
                # delete this position and append left and right positions
                tmp_pos.append(pos+1)
                tmp_pos.append(pos-1)
                total += 1
                validate_grid[row+1, pos+1] = 9
                validate_grid[row+1, pos-1] = 9
            else:
                # continue at this position
                tmp_pos.append(pos)
                validate_grid[row+1, pos] = 9
        beam_positions = list(set(tmp_pos))
    return total

def run_part2(input_file):
    inp = input_reader2(input_file)
    mapping = {'.': 0, '^': 1, 'S': 3}
    grid = np.asarray([[mapping[i] for i in n] for n in inp]).astype(int)
    # validate_grid = np.copy(grid)     # this was just for debugging to see the paths
    start_pos = [p[0] for p in np.where(grid == 3)]
    beam_positions = [start_pos[1]]
    counts = [1]
    for row in range(grid.shape[0]-1):
        tmp_pos = []
        tmp_counts = []
        for pos, c in zip(beam_positions, counts):
            if grid[row+1, pos] == 1:
                # delete this position and append left and right positions
                tmp_pos.append(pos+1)
                tmp_counts.append(c)
                tmp_pos.append(pos-1)
                tmp_counts.append(c)
                # validate_grid[row+1, pos+1] = 9
                # validate_grid[row+1, pos-1] = 9
            else:
                # continue at this position
                tmp_pos.append(pos)
                tmp_counts.append(c)
                # validate_grid[row+1, pos] = 9
        counts = defaultdict(int)
        for value, extra in zip(tmp_pos, tmp_counts):
            counts[value] += extra
        counts_values = np.asarray([[value, total] for value, total in counts.items()])
        counts = counts_values[:, 1]
        beam_positions = counts_values[:, 0]
    return np.sum(counts)

if __name__ == '__main__':
    print(f'Solution to task 7.1 is {run_part1(input_file="aoc_07_input.txt")}')
    print(f'Solution to task 7.2 is {run_part2(input_file="aoc_07_input.txt")}')