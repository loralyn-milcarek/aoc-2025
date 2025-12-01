import sys
import os
from datetime import datetime

def create_day_files(day):
    """
    Create solution and input files for a specific day.
    Usage: python create_day.py [day_number]
    If no day number is provided, uses today's date.
    """
    if day < 1 or day > 12:
        print(f"Error: Day must be between 1 and 12 (got {day})")
        return False
    
    template = '''import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_input, read_lines

def parse_input(day):
    """Parse the input file for this day."""
    lines = read_lines(day)
    # TODO: Parse input
    return lines

def part1(data):
    """Solve part 1."""
    # TODO: Implement solution
    pass

def part2(data):
    """Solve part 2."""
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    day = {day}
    data = parse_input(day)
    
    print(f"Day {{day}}")
    print(f"Part 1: {{part1(data)}}")
    print(f"Part 2: {{part2(data)}}")
'''
    
    # Create solution file
    solution_path = f"solutions/{day:02d}.py"
    if os.path.exists(solution_path):
        print(f"Solution file already exists: {solution_path}")
    else:
        with open(solution_path, "w") as f:
            f.write(template.format(day=day))
        print(f"Created {solution_path}")
    
    # Create empty input file
    input_path = f"input/{day:02d}.txt"
    if os.path.exists(input_path):
        print(f"Input file already exists: {input_path}")
    else:
        with open(input_path, "w") as f:
            f.write("")
        print(f"Created {input_path}")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            day = int(sys.argv[1])
        except ValueError:
            print("Error: Day must be a number")
            sys.exit(1)
    else:
        day = datetime.now().day
    
    if create_day_files(day):
        print(f"Day {day:02d} files created!")
   