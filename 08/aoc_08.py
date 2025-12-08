""" AOC 2025 day 8 """

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
    # inp = input_reader2(input_file)
    in_df = pd.read_csv(input_file, header=None)
    in_df.columns = ['x', 'y', 'z']
    # plt.scatter(in_df['x'], in_df['y'], c=in_df['z'])
    # plt.show(block=True)
    distances = {}
    for (i, p1), (j, p2) in itertools.combinations(enumerate(in_df.to_numpy()), 2):
        p1 = np.array(p1)
        p2 = np.array(p2)
        d = np.linalg.norm(p1 - p2)
        distances[(i, j)] = d

    connections = []
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    for i in range(1000):
        curr_elem = sorted_distances[i]
        connections.append(curr_elem[0])
    G = nx.Graph()
    G.add_edges_from(connections)
    components = list(nx.connected_components(G))
    the_rest = in_df.shape[0] - np.sum([len(i) for i in components])
    largest_sizes = sorted([len(i) for i in components])[::-1][:3]
    total = np.prod(largest_sizes)
    return total

def run_part2(input_file):
    in_df = pd.read_csv(input_file, header=None)
    in_df.columns = ['x', 'y', 'z']
    # plt.scatter(in_df['x'], in_df['y'], c=in_df['z'])
    # plt.show(block=True)
    distances = {}
    for (i, p1), (j, p2) in itertools.combinations(enumerate(in_df.to_numpy()), 2):
        p1 = np.array(p1)
        p2 = np.array(p2)
        d = np.linalg.norm(p1 - p2)
        distances[(i, j)] = d

    connections = []
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    for i in range(len(sorted_distances)):
        curr_elem = sorted_distances[i]
        connections.append(curr_elem[0])
        G = nx.Graph()
        G.add_edges_from(connections)
        components = list(nx.connected_components(G))
        the_rest = 1 if np.sum([len(i) for i in components]) == in_df.shape[0] else 0
        if the_rest:
            last_points = curr_elem[0]
            break
    total = in_df['x'][last_points[0]] * in_df['x'][last_points[1]]
    return total

if __name__ == '__main__':
    print(f'Solution to task 8.1 is {run_part1(input_file="aoc_08_input.csv")}')
    print(f'Solution to task 8.2 is {run_part2(input_file="aoc_08_input.csv")}')