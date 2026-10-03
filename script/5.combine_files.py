#!/usr/bin/env python3
import os

def combine_and_remove_duplicates(directory, output_file):
    """Combines all .txt files in a directory, removes duplicates, and saves to a new file."""
    unique_lines = set()
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
                for line in file:
                    unique_lines.add(line.strip())
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in sorted(unique_lines):
            outfile.write(line + '\n')

# Example Usage
directory_path = '../processed/blocklist'
output_filepath = '../combined/blocklist.txt'
combine_and_remove_duplicates(directory_path, output_filepath)

directory_path = '../processed/allowlist'
output_filepath = '../combined/allowlist.txt'
combine_and_remove_duplicates(directory_path, output_filepath)