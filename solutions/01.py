import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_input, read_lines

def parse_input(day):
    return read_lines(day)

def count_zeros(instructions):
    zero_count = 0
    current_position = 50
    for line in instructions:
        direction, move = line[0], int(line[1:][-2:])

        if direction == "L":
            current_position = (current_position - move) % 100
        else:
            current_position = (current_position + move) % 100
        zero_count += (current_position == 0)
    return zero_count

def count_zeros_passed(data):
    """
    Count how many times position 0 is landed on or crossed on a circular dial numbered 0-99.
    
    Args:
        List of strings containing direction (L or R) followed by distance to move.
    
    Returns:
        Total number of times position 0 is encountered
    """
    zero_count = 0
    current_position = 50

    for line in data:
        direction, revolutions, move = line[0], line[1:-2], int(line[1:][-2:])
        move *= -1 if direction == "L" else 1
        zero_count += int(revolutions) if revolutions else 0
        target = current_position + move
        if current_position != 0:
            if (target < 0 and target > -100) or (target > 100 and target < 200):
                zero_count += 1
            if target <= -100 or target >= 200:
                zero_count += target // 100
        current_position = target % 100
        zero_count += (current_position == 0)

    return zero_count

if __name__ == "__main__":
    day = 1
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {count_zeros(data)}")
    print(f"Part 2: {count_zeros_passed(data)}")
