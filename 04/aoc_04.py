""" AOC 2025 day 4 """
import numpy as np
import time
from scipy.signal import convolve2d

def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def input_reader2(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]

def run_part1(input_file):
    inp = input_reader2(input_file)
    replacing = {'.': 0, '@': 1}
    grid = np.asarray([[replacing[c] for c in i] for i in inp])
    kernel = np.asarray([[1, 1, 1],
                         [1, 0, 1],
                         [1, 1, 1]])
    result = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    result[result >= 4] = -1
    final_res = ((result+1) * grid).astype('bool') * 1
    res = np.sum(final_res)
    return res

def run_part2(input_file):
    inp = input_reader2(input_file)
    replacing = {'.': 0, '@': 1}
    grid = np.asarray([[replacing[c] for c in i] for i in inp])
    kernel = np.asarray([[1, 1, 1],
                         [1, 0, 1],
                         [1, 1, 1]])
    n_removed = 0
    for i in range(grid.shape[0] * grid.shape[1]):
        result = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
        result[result >= 4] = -1
        final_res = ((result + 1) * grid).astype('bool') * 1
        res = np.sum(final_res)
        n_removed += res
        grid = (grid * (final_res*-1 + 1))
        if res == 0:
            break
    return n_removed

if __name__ == '__main__':
    print(f'Solution to task 4.1 is {run_part1(input_file="aoc_04_input.txt")}')
    print(f'Solution to task 4.2 is {run_part2(input_file="aoc_04_input.txt")}')