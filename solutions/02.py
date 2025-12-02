import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_blocks

def parse_input(day):
    """Parse the comma-separated input file."""
    lines = read_blocks(day, ",")
    return lines

def find_invalid_ids(id_ranges):
    """
    Finds and sums all invalid IDs in given ranges.
    Invalid IDs are pairs of repeated digits (e.g. 11, 1010, 1188511885)

    Arguments: 
        ranges: List of ranges (numbers stored as string) to check for invalid IDs

    Returns: Sum of all invalid IDs
    """
    invalid_ids = []

    for id_range in id_ranges:
        # Check all possible IDs in range
        start, end = id_range.split("-")

        for id in range(int(start), int(end) + 1):
            id = str(id)

            # Skip odd lengths
            if len(id) % 2 != 0:
                continue
            
            # Find midpoint
            mid = len(id) // 2

            # Compare halves
            if id[mid:] == id[:mid]:
                invalid_ids.append(int(id))

    return sum(invalid_ids)



def part2(data):
    """Solve part 2."""
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    day = 2
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {find_invalid_ids(data)}")
    print(f"Part 2: {part2(data)}")
