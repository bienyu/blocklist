#!/usr/bin/env python3

def remove_lines(file1_path, file2_path, output_path):
    """Removes lines from file1 that are present in file2 and writes the result to a new file."""
    try:
        with open(file1_path, 'r', encoding='utf-8', errors='replace') as file1, open(file2_path, 'r', encoding='utf-8', errors='replace') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

        unique_lines = [line for line in file1_lines if line not in file2_lines]

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(unique_lines)
        
        return True
    
    except FileNotFoundError:
        return False

# Example usage
file1_path = '../combined/blocklist.txt'
file2_path = '../combined/allowlist.txt'
output_path = '../blocklist.txt'

# Create dummy files for the example
# with open(file1_path, 'w') as f:
#     f.write("line 1\nline 2\nline 3\nline 4\n")
# with open(file2_path, 'w') as f:
#     f.write("line 2\nline 4\n")

if remove_lines(file1_path, file2_path, output_path):
    print(f"Lines removed and saved to {output_path}")
else:
    print("One or both input files not found.")