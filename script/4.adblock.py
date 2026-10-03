#!/usr/bin/env python3
import os

def extract_domains(input_file, output_file):
    extracted_domains = []

    with open(input_file, 'r', encoding='utf-8', errors='replace') as infile:
        for line in infile:
            line = line.strip()
            if line.startswith('!') or line.startswith('[') or not line:  # Skip comments, metadata, and empty lines
                continue
            if line.startswith('||'):  # Adblock-style domain rule
                domain = line.split('^')[0][2:].replace('*','')  # Extract domain after '||' and before '^'
                extracted_domains.append(domain)
            elif line.startswith('##[href^="http://') or line.startswith('##[href^="https://'):  # CSS rules
                domain = line.split('"')[1].replace('http://', '').replace('https://', '').split('/')[0].replace('*','')
                extracted_domains.append(domain)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(extracted_domains))

    print(f"Extracted {len(extracted_domains)} domains to {output_file}")

# Input and output file paths
for hosts_file in os.listdir('../raw/blocklist/adguard'):
    input_file = f'../raw/blocklist/adguard/{hosts_file}'
    output_file = f'../processed/blocklist/domains_only_{hosts_file}.txt'
    extract_domains(input_file, output_file)

for hosts_file in os.listdir('../raw/allowlist/adguard'):
    input_file = f'../raw/allowlist/adguard/{hosts_file}'
    output_file = f'../processed/allowlist/domains_only_{hosts_file}.txt'
    extract_domains(input_file, output_file)