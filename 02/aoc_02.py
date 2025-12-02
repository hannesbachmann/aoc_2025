""" AOC 2025 day 2 """


def input_reader(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '').split(',')

def run_part1(input_file):
    inp = input_reader(input_file)
    min_max = [s.split('-') for s in inp]
    selection = []
    for min_v, max_v in min_max:
        start = int(min_v)
        for code in range(start, int(max_v)+1, 1):
            s_code = str(code)
            if len(s_code) % 2 == 0 and s_code[:int(len(s_code)/2)] == s_code[int(len(s_code)/2):]:
                selection.append(code)
    return sum(selection)

def run_part2(input_file):
    inp = input_reader(input_file)
    min_max = [s.split('-') for s in inp]
    selection = []
    for min_v, max_v in min_max:
        start = int(min_v)
        for code in range(start, int(max_v)+1, 1):
            s_code = str(code)
            invalid_id = False
            for l in range(1, int(len(s_code)/2)+1):
                curr_seq = s_code[:l]
                match_break = False
                for s_i in range(l, len(s_code), l):
                    seq = s_code[s_i:s_i+l]
                    if seq != curr_seq:
                        match_break = True
                        break
                if not match_break:
                    invalid_id = True
                    break
            if invalid_id:
                selection.append(code)

    return sum(selection)

if __name__ == '__main__':
    inp = input_reader('aoc_02_example.txt')
    print(f'Solution to task 2.1 is {run_part1(input_file="aoc_02_input.txt")}')
    print(f'Solution to task 2.2 is {run_part2(input_file="aoc_02_input.txt")}')