import re
import os

def check_solution(day):
    """Check if a solution file has part1 and part2 implemented."""
    filepath = f"solutions/{day:02d}.py"
    if not os.path.exists(filepath):
        return "⬜", "⬜"
    
    with open(filepath) as f:
        content = f.read()
    
    # Check if parts have been completed
    part1_done = "def part1" not in content
    part2_done = "def part2" not in content
    
    part1_status = "✅" if part1_done else "⬜"
    part2_status = "✅" if part2_done else "⬜"
    
    return part1_status, part2_status

def update_readme():
    """Update the progress table in README.md"""
    with open("README.md") as f:
        readme = f.read()
    
    # Build progress table (only 12 days for AoC 2025)
    table = "| Day | Part 1 | Part 2 |\n|-----|--------|--------|\n"
    
    for day in range(1, 13):
        part1, part2 = check_solution(day)
        table += f"| {day:02d}  | {part1} | {part2} |\n"
    
    # Replace content between markers
    pattern = r"<!-- PROGRESS_TABLE_START -->.*?<!-- PROGRESS_TABLE_END -->"
    replacement = f"<!-- PROGRESS_TABLE_START -->\n{table}<!-- PROGRESS_TABLE_END -->"
    
    updated_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)
    
    with open("README.md", "w") as f:
        f.write(updated_readme)
    
    print("✓ Updated progress table in README.md")

if __name__ == "__main__":
    update_readme()
