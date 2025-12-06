import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_lines

def parse_input(day):
    """Parse the input file for this day."""
    lines = read_lines(day)
    return lines

def find_max_joltage(banks, num_batteries = 2):
    """
    Finds largest possible joltage for each bank.

    Arguments:
        banks: List of battery bank jolts. Each digit represents the joltage of a single battery.
        num_batteries: Number of batteries to include from each bank. Defaults to 2.

    Returns:
        Sum of all bank max joltage results.
    """
    max_jolts = []

    for bank in banks:
        on_jolts = ""
        batteries_remaining = num_batteries
        start = 0

        while batteries_remaining > 0 and start < len(bank):
            max_jolt = '0'
            end = len(bank) - batteries_remaining + 1

            for i in range(start, end):
                jolt = bank[i]
                if jolt > max_jolt:
                    max_jolt, start = jolt, i
                if max_jolt == '9':
                    break
            
            start += 1
            batteries_remaining -= 1
            on_jolts += max_jolt
            
        max_jolts.append(int(on_jolts))
            
    return sum(max_jolts)    

if __name__ == "__main__":
    day = 3
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {find_max_joltage(data)}")
    print(f"Part 2: {find_max_joltage(data, 12)}")
