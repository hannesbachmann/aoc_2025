""" AOC 2025 day 9 """

import numpy as np
from collections import defaultdict
import time
import re
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import networkx as nx

def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def input_reader2(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]

def run_part1(input_file):
    in_df = pd.read_csv(input_file, header=None)
    in_df.columns = ['x', 'y']

    areas = {}
    for (i, p1), (j, p2) in itertools.combinations(enumerate(in_df.to_numpy()), 2):
        p1 = np.array(p1)
        p2 = np.array(p2)
        a = (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)
        areas[(i, j)] = a
    sorted_areas = sorted(areas.items(), key=lambda item: item[1])[-1]
    max_area = sorted_areas[1]
    return max_area

def run_part2(input_file):
    in_df = pd.read_csv(input_file, header=None)
    in_df.columns = ['x', 'y']
    return 0

if __name__ == '__main__':
    print(f'Solution to task 9.1 is {run_part1(input_file="aoc_09_input.csv")}')
    # print(f'Solution to task 9.2 is {run_part2(input_file="aoc_09_input.csv")}')