def read_input(day):
    """Read raw input file."""
    with open(f"input/{day:02d}.txt") as f:
        return f.read().strip()

def read_lines(day):
    """Read input as list of lines."""
    return read_input(day).split("\n")

def read_grid(day):
    """Read input as 2D grid of characters."""
    return [list(row) for row in read_lines(day)]

def read_blocks(day: int, separator: str = "\n\n") -> list[str]:
    """Read input split by blank lines or custom separator."""
    return read_input(day).split(separator)