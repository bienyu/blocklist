#!/usr/bin/env python3
import os

def extract_domains(input_file, output_file):
    extracted_domains = []

    with open(input_file, 'r', encoding='utf-8', errors='replace') as infile:
        for line in infile:
            line = line.strip()
            
            if line.startswith('#') or line.startswith('//') or not line:  # Skip comments and empty lines
                continue
            domain = line.split()[0].replace('*','')  # Extract the first part of the line (the domain)
            extracted_domains.append(domain)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(extracted_domains))

    print(f"Extracted {len(extracted_domains)} domains to {output_file}")

# Input and output file paths
for hosts_file in os.listdir('../raw/blocklist/plain'):
    input_file = f'../raw/blocklist/plain/{hosts_file}'
    output_file = f'../processed/blocklist/domains_only_{hosts_file}.txt'
    extract_domains(input_file, output_file)

for hosts_file in os.listdir('../raw/allowlist/plain'):
    input_file = f'../raw/allowlist/plain/{hosts_file}'
    output_file = f'../processed/allowlist/domains_only_{hosts_file}.txt'
    extract_domains(input_file, output_file)