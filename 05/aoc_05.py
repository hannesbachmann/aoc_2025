""" AOC 2025 day 5 """

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
    ranges = np.asarray([i.split('-') for i in inp if ('-' in i)])
    nums = np.asarray([int(i) for i in inp if ('-' not in i) and (i != '')])
    ranges = ranges.astype(np.int64)

    idx = 0
    for n in nums:
        for start, end in ranges:
            if start <= n <= end:
                idx += 1
                break

    return idx

def run_part2(input_file):
    inp = input_reader2(input_file)
    ranges = np.asarray([i.split('-') for i in inp if ('-' in i)])
    ranges = ranges.astype(np.int64)

    ranges = np.sort(ranges, axis=0)
    s, e = ranges[0, :]
    total_diff = 0
    for start, end in ranges[1:,:]:
        if start == e:
            total_diff += (e-s)
            s = start
            e = end
        elif start > e:
            total_diff += (e-s + 1)
            s = start
            e = end
        elif start < e < end:
            e = end
    total_diff += (e-s + 1)
    return total_diff

if __name__ == '__main__':
    print(f'Solution to task 5.1 is {run_part1(input_file="aoc_05_input.txt")}')
    print(f'Solution to task 5.2 is {run_part2(input_file="aoc_05_input.txt")}')