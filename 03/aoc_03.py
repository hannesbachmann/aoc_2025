""" AOC 2025 day 3 """
import numpy as np

def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]


def run_part1(input_file):
    inp = input_reader(input_file)
    digits = np.asarray([[int(i) for i in line] for line in inp])
    first_pos = np.argmax(digits[:,:-1], axis=1)
    second_pos = [np.argmax(digits[i,first_p+1:])+first_p+1 for i, first_p in enumerate(first_pos)]
    first = [digits[i, f_pos] for i, f_pos in enumerate(first_pos)]
    second = [digits[i, s_pos] for i, s_pos in enumerate(second_pos)]
    first_second_sum = np.sum([int(str(f) + str(s)) for f, s in zip(first, second)])
    return first_second_sum


def run_part2(input_file):
    inp = input_reader(input_file)
    digits = np.asarray([[int(i) for i in line] for line in inp])
    selected_positions = np.zeros(shape=(digits.shape[0], 12), dtype=int)
    selected_values = ['' for _ in range(digits.shape[0])]
    for n_pos in range(12):
        for n_l, l in enumerate(digits):
            if n_pos == 0:
                last_pos = 0
            else:
                last_pos = selected_positions[n_l,n_pos-1]+1
            selected_positions[n_l,n_pos] = np.argmax(digits[n_l,last_pos:digits.shape[1]-(12-(n_pos+1))]) + last_pos
            selected_values[n_l] = selected_values[n_l] + str(digits[n_l,selected_positions[n_l,n_pos]])

    selected_sum = sum([int(v) for v in selected_values])
    return selected_sum

if __name__ == '__main__':
    print(f'Solution to task 2.1 is {run_part1(input_file="aoc_03_input.txt")}')
    print(f'Solution to task 2.2 is {run_part2(input_file="aoc_03_input.txt")}')