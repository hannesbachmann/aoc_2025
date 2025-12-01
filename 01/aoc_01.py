""" AOC 2025 day 1 """


def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [l.replace('\n', '') for l in f.readlines()]

def turn_dial(curr_loc, direction, distance):
    # for part1
    tmp_loc = curr_loc
    if direction == 'L':
        tmp_loc = (curr_loc - distance + 100) % 100
    if direction == 'R':
        tmp_loc = (curr_loc + distance) % 100
    return tmp_loc

def turn_dial_with_count(curr_loc, direction, distance):
    # for part2
    tmp_loc = curr_loc
    n_zeros = 0
    if direction == 'L':
        a = distance - tmp_loc
        n_zeros = (a + 100) // 100
        if tmp_loc == 0:
            n_zeros -= 1
        tmp_loc = (curr_loc - distance + 100) % 100
    if direction == 'R':
        a = distance + tmp_loc
        n_zeros = a // 100
        tmp_loc = (curr_loc + distance) % 100
    return tmp_loc, n_zeros

def run_part1(input_file: str):
    input = input_reader(input_file)
    dists = [int(inp.replace('L', '').replace('R', '')) for inp in input]
    dirs = [inp[0] for inp in input]
    dir_dis = [[dir, dist] for dir, dist in zip(dirs, dists)]

    total_zeros = 0
    curr_loc = 50
    for dir, dis in dir_dis:
        curr_loc = turn_dial(curr_loc, dir, dis)
        if curr_loc == 0:
            total_zeros += 1
        print(curr_loc)
    print(total_zeros)
    return total_zeros

def run_part2(input_file: str):
    input = input_reader(input_file)
    dists = [int(inp.replace('L', '').replace('R', '')) for inp in input]
    dirs = [inp[0] for inp in input]
    dir_dis = [[dir, dist] for dir, dist in zip(dirs, dists)]

    total_zeros = 0
    curr_loc = 50
    for dir, dis in dir_dis:
        curr_loc, n_zeros = turn_dial_with_count(curr_loc, dir, dis)
        total_zeros += n_zeros
        print(curr_loc)
        print(f'n_zeros: {n_zeros}')
    print(total_zeros)
    return total_zeros

if __name__ == '__main__':
    print(f'Solution to task 1.1 is {run_part1(input_file="aoc_01_input.txt")}')
    print(f'Solution to task 1.2 is {run_part2(input_file="aoc_01_input.txt")}')