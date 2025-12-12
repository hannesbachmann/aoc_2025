""" AOC 2025 day 11 """

import numpy as np
import networkx as nx

def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def input_reader2(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]

def run_part1(input_file):
    inp = input_reader2(input_file)
    devices = [i[0:3] for i in inp]
    outputs = [i[5:].split(' ') for i in inp]

    edges = []
    for i, d in enumerate(devices):
        for o in outputs[i]:
            edges.append((d, o))

    G = nx.DiGraph()
    G.add_edges_from(edges)
    all_paths = list(nx.all_simple_paths(G, source='you', target='out'))
    total = len(all_paths)
    return total

def run_part2(input_file):
    inp = input_reader2(file_name=input_file)
    return 0


if __name__ == '__main__':
    print(f'Solution to task 11.1 is {run_part1(input_file="aoc_11_input.txt")}')
    # print(f'Solution to task 11.2 is {run_part2(input_file="aoc_11_input.txt")}')
