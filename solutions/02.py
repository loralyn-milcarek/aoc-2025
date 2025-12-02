import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_blocks

def parse_input(day):
    """Parse the comma-separated input file."""
    lines = read_blocks(day, ",")
    return lines

def find_invalid_doubled_ids(id_ranges):
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



def find_invalid_repeated_ids(id_ranges):
    invalid_ids = []

    for id_range in id_ranges:
        start, end = id_range.split("-")

        for id in range(int(start), int(end) + 1):
            id_string = str(id)
            id_length = len(id_string)

            for pattern_length in range(1, (id_length // 2) + 1):
                if id_length % pattern_length != 0:
                    continue
                
                repeat = id_length // pattern_length
                pattern = id_string[:pattern_length]

                if pattern * repeat == id_string:
                    invalid_ids.append(int(id))
                    break

    return sum(invalid_ids)

if __name__ == "__main__":
    day = 2
    data = parse_input(day)

    print(f"Day {day}")
    print(f"Part 1: {find_invalid_doubled_ids(data)}")
    print(f"Part 2: {find_invalid_repeated_ids(data)}")
