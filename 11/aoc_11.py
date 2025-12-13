""" AOC 2025 day 11 """
import time
import numpy as np
import networkx as nx
from numba import njit
from collections import Counter, defaultdict, deque
from functools import cache

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
    devices = [i[0:3] for i in inp]
    outputs = [i[5:].split(' ') for i in inp]
    ids = {dev: i for i, dev in enumerate(devices) if dev not in ['out', 'fft', 'dac', 'svr']}
    for i, dev in enumerate(['out', 'fft', 'dac', 'svr']):
        ids[dev] = -1 * (i+1)

    edges = []
    for i, d in enumerate(devices):
        for o in outputs[i]:
            edges.append((ids[d], ids[o]))

    # now we must by starting from svr also visit the edges fft and dac before ending in out
    # possible path types:
    # 1. svr -> ... -> fft -> ... -> dac -> ... -> out
    # 1. svr -> ... -> dac -> ... -> fft -> ... -> out
    G = nx.DiGraph()
    G.add_edges_from(edges)
    G_rev = G.reverse()
    type1_part1 = nx.shortest_simple_paths(G_rev, source=-1, target=-3)
    type1_part2 = nx.shortest_simple_paths(G_rev, source=-3, target=-2)
    type1_part3 = nx.shortest_simple_paths(G_rev, source=-2, target=-4)
    # no path between fft and dac (in the reverse Graph) -> not need to calculate out -> fft and dac -> svr
    idx = 0
    time_start = time.time()
    while True:
        try:
            next(type1_part1)
        except:
            break
        if idx % 1000 == 0:
            print(idx, time.time() - time_start)
            time_start = time.time()
        idx += 1
    total1 = idx
    print(total1)   # 4811
    idx = 0
    time_start = time.time()
    while True:
        try:
            next(type1_part2)
        except:
            break
        if idx % 1000 == 0:
            print(idx, time.time() - time_start)
            time_start = time.time()
        idx += 1
    total2 = idx
    print(total2)   # 25106
    idx = 0
    time_start = time.time()
    while True:
        try:
            next(type1_part3)
        except:
            break
        if idx % 1000 == 0:
            print(idx, time.time() - time_start)
            time_start = time.time()
        idx += 1
    total3 = idx
    print(total3)   # 3879
    return total1 * total2 * total3

if __name__ == '__main__':
    print(f'Solution to task 11.1 is {run_part1(input_file="aoc_11_input.txt")}')
    print(f'Solution to task 11.2 is {run_part2(input_file="aoc_11_input.txt")}')
