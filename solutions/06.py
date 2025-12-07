import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_lines, read_transposed_grid_whitespace_separated
from math import prod
import re

def parse_input_part1(day):
    lines = read_transposed_grid_whitespace_separated(day)
    return lines

def parse_input_part2(day):
    lines = read_lines(day)
    rows = list(map(lambda l: list(l), lines))
    problems = []
    curr_problem = []
    while len(rows[0]):
        curr_num = ""
        operator = ""
        for row in rows:
            char = row.pop() if len(row) else " "
            if char == " ":
                continue
            if char == "+" or char == "*":
                operator = char
            else:
                curr_num += char
        if curr_num:
            curr_problem.append(curr_num)
            curr_num = ""
        if operator:
            curr_problem.append(operator)
            problems.append(curr_problem)
            curr_problem = []
            operator = ""
    return problems

def do_cephalopod_math(problems):
    """
    Solves math problems given a list of numbers and operators.

    Arguments:
        problems: 2D list of problems containing numbers followed by an addition or multiplication operator.

    Returns: Sum of all problem solutions.
    """
    total = 0
    for problem in problems:
        should_add = problem.pop() == "+"
        numbers = list(map(lambda n: int(n), problem))
        total += sum(numbers) if should_add else prod(numbers)
    return total

if __name__ == "__main__":
    day = 6
    data_part1 = parse_input_part1(day)
    data_part2 = parse_input_part2(day)
    
    print(f"Day {day}")
    print(f"Part 1: {do_cephalopod_math(data_part1)}")
    print(f"Part 2: {do_cephalopod_math(data_part2)}")
