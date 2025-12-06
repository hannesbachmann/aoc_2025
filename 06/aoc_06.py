""" AOC 2025 day 6 """

import numpy as np
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
    nums = np.asarray([re.findall('[0-9]+', i) for i in inp[:-1]]).astype(int)
    operations = [i for i in inp[-1] if i in ['+', '*']]
    total = 0
    for i, op in enumerate(operations):
        if op == '+':
            total += np.sum(nums[:, i])
        else:
            total += np.prod(nums[:, i])
    return total

def run_part2(input_file):
    inp = input_reader2(input_file)
    # line ' '-padding to tangle issues with cutted ' ' at the end
    max_line_len = max([len(i) for i in inp])
    inp = [line.ljust(max_line_len) for line in inp]
    operations = [i for i in inp[-1] if i in ['+', '*']]

    # process the input by focusing on the spacing
    nums = inp[:-1]
    op_line = inp[-1]

    op_positions = [i for i, ch in enumerate(op_line) if ch in ['*', '+']]
    op_positions.append(len(op_line)+2)

    boundaries = [(op_positions[i], op_positions[i + 1]) for i in range(len(op_positions) - 1)]

    result = []
    for row in nums:
        row_substrings = []
        for start, end in boundaries:
            segment = row[start:end-1]
            row_substrings.append(segment)
        result.append(row_substrings)

    in_nums = np.asarray(result)
    total = 0
    for i, op in enumerate(operations):
        max_len = max(len(s) for s in in_nums[:, i])
        digits = ['' for _ in range(max_len)]
        for d in range(max_len):
            for j in range(in_nums.shape[0]):
                digits[d] = digits[d] + in_nums[j, i][d]
        digit_values = np.asarray(digits).astype(int)
        if op == '+':
            total += np.sum(digit_values)
        else:
            total += np.prod(digit_values)

    return total

if __name__ == '__main__':
    print(f'Solution to task 6.1 is {run_part1(input_file="aoc_06_input.txt")}')
    print(f'Solution to task 6.2 is {run_part2(input_file="aoc_06_input.txt")}')