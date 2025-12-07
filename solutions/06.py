import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_transposed_grid_whitespace_separated
from math import prod

def parse_input(day):
    """Parse the input file for this day."""
    lines = read_transposed_grid_whitespace_separated(day)
    # print(lines)
    return lines

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

def part2(data):
    """Solve part 2."""
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    day = 6
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {do_cephalopod_math(data)}")
    print(f"Part 2: {part2(data)}")
