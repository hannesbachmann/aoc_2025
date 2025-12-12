""" AOC 2025 day 10 """

import numpy as np
import itertools
import pulp

def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def input_reader2(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]

def run_part1(input_file):
    inp = input_reader2(file_name=input_file)
    inp_split = [i.split(' ') for i in inp]
    repl = {'.': 0, '#': 1}
    lights = [np.asarray([repl[s] for s in l[0][1:-1]]) for l in inp_split]
    buttons = [[[int(j) for j in s[1:-1].split(',')] for s in l[1:-1]] for l in inp_split]
    joltages = [[int(s) for s in l[-1][1:-1] if s != ','] for l in inp_split]   # not needed fo rnow
    vector_lengths = [len(l) for l in lights]
    button_vectors = [np.asarray([[int(i in bpos) for i in range(vl)] for bpos in blist]) for blist, vl in zip(buttons, vector_lengths)]

    # (a*button[0] + b*button[1] + c*button[2] + ... + d*button[n]) mod 2 = light
    # find a, b, c, ..., n
    total_best_combinations = []
    total_best_costs = []
    for n in range(len(lights)):
        combinations = itertools.product('01', repeat=len(button_vectors[n]))

        button = button_vectors[n]
        light = lights[n]
        best_cost = 10000
        best_combi = None
        for c in combinations:
            cost = sum([int(i) for i in c])
            if cost > best_cost:
                continue
            total = sum([int(c[i])*button[i] for i in range(len(c))]) % 2
            if np.sum(np.abs(np.subtract(total, light))) == 0:
                combi = c
                if cost <= best_cost:
                    best_cost = cost
                    best_combi = combi
        total_best_combinations.append(best_combi)
        total_best_costs.append(best_cost)
    result = sum(total_best_costs)
    return result

def run_part2(input_file):
    inp = input_reader2(file_name=input_file)
    inp_split = [i.split(' ') for i in inp]
    repl = {'.': 0, '#': 1}
    lights = [[repl[s] for s in l[0][1:-1]] for l in inp_split]
    buttons = [[[int(j) for j in s[1:-1].split(',')] for s in l[1:-1]] for l in inp_split]
    joltages = [np.asarray([int(j) for j in l[-1][1:-1].split(',')]) for l in inp_split]
    vector_lengths = [len(l) for l in lights]
    button_vectors = [np.asarray([[int(i in bpos) for i in range(vl)] for bpos in blist]) for blist, vl in
                      zip(buttons, vector_lengths)]

    # (a*button[0] + b*button[1] + c*button[2] + ... + d*button[n]) = joltage
    # find a, b, c, ..., d

    result = 0
    for n in range(len(lights)):
        joltage = joltages[n]
        max_spec_cost = [np.min(joltage[i]) for i in buttons[n]]
        button = button_vectors[n]

        best_cost = alternative_solve_lgs(np.column_stack(button), joltage, max_spec_cost)
        result += best_cost
    return result

def alternative_solve_lgs(A, b, upper_bounds):
    n = len(upper_bounds)

    model = pulp.LpProblem("LGS solutions", pulp.LpStatusOptimal)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, upBound=upper_bounds[i], cat=pulp.LpInteger)
         for i in range(n)]

    for row, rhs in zip(A, b):
        model += pulp.lpSum(row[i] * x[i] for i in range(n)) == rhs

    model += 0

    solver = pulp.PULP_CBC_CMD(msg=False)

    # Solve
    status = model.solve(solver=solver)

    sol_cost = 1000000
    while True:
        status = model.solve()

        if pulp.LpStatus[status] != "Optimal":
            break

        sol = tuple(int(v.value()) for v in x)
        cost = sum(sol)
        if cost < sol_cost:
            sol_cost = cost
            print(sol_cost)

        model += pulp.lpSum(x) <= sol_cost-1
    return sol_cost

if __name__ == '__main__':
    # print(f'Solution to task 10.1 is {run_part1(input_file="aoc_10_input.txt")}')
    print(f'Solution to task 10.2 is {run_part2(input_file="aoc_10_input.txt")}')
    # 18979