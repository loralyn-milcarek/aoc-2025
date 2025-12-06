import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_input, read_lines

def parse_input(day):
    """Parse the input file for this day."""
    lines = read_lines(day)
    return lines

def find_max_joltage(banks):
    """
    Finds largest possible joltage for each bank. 

    Arguments:
        banks: List of battery bank jolts. Each digit represents the joltage of a single battery.

    Returns:
        Sum of all bank max joltage results.
    """
    max_jolts = []

    for bank in banks:
        max_a, index_a = '0', 0
        max_b = '0'

        for i in range(index_a, len(bank) - 1):
            jolt = bank[i]
            if jolt > max_a:
                max_a, index_a = jolt, i
            if max_a == 9:
                break

        for i in range(index_a + 1, len(bank)):
            jolt = bank[i]
            if jolt > max_b:
                max_b = jolt
            if max_b == 9:
                break
    
        max_jolts.append(int(max_a + max_b))
    
    return sum(max_jolts)    


if __name__ == "__main__":
    day = 3
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {find_max_joltage(data)}")
