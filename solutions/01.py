import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_input, read_lines

def parse_input(day):
    return read_lines(day)

def part1(data):
    zeros = 0
    start = 50
    for line in data:
        direction, move = line[0], int(line[1:][-2:])

        if direction == "L":
            start = (start - move) % 100
        else:
            start = (start + move) % 100
        zeros += (start == 0)
    return zeros

def part2(data):
    """Solve part 2."""
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    day = 1
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {part1(data)}")
    # print(f"Part 2: {part2(data)}")
