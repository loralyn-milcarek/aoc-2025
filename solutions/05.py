import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_input, read_lines, read_blocks

def parse_input(day):
    """Parse the input file for this day."""
    blocks = read_blocks(day)
    fresh_ranges = [
        tuple(map(int, r.split('-')))
        for r in blocks[0].split("\n")
    ]
    ids = list(map(int, blocks[1].split("\n")))
    return fresh_ranges, ids

def count_valid_ids(fresh_ranges, ids):
    """
    Counts valid IDs that are in one or more of the fresh ranges.

    Arguments: 
        fresh_ranges: list of tuples with start and end range
        ids: list of ints

    Returns:
        Fresh ID count
    """
    fresh_count = 0
    for id in ids:
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= id <= fresh_range[1]:
                fresh_count += 1
                break
    return fresh_count
            
def part2(fresh_ranges, ids):
    """Solve part 2."""
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    day = 5
    ranges, ids = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {count_valid_ids(ranges, ids)}")
    # print(f"Part 2: {part2(ranges, ids)}")
