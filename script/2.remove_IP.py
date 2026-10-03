#!/usr/bin/env python3
import re, os

def extract_domains(input_file, output_file):
    domain_pattern_1 = re.compile(r'^0\.0\.0\.0\s+([\w.-]+)')  # Matches "0.0.0.0 domain.com"
    domain_pattern_2 = re.compile(r'^127\.0\.0\.1\s+([\w.-]+)')  # Matches "127.0.0.1 domain.com"
    extracted_domains = []

    with open(input_file, 'r', encoding='utf-8', errors='replace') as infile:
        for line in infile:
            line = line.strip()
            if line.startswith('#') or not line:  # Skip comments and empty lines
                continue
            match_1 = domain_pattern_1.match(line)
            if match_1:
                extracted_domains.append(match_1.group(1).replace('*',''))  # Extract domain
            match_2 = domain_pattern_2.match(line)
            if match_2:
                extracted_domains.append(match_2.group(1).replace('*',''))  # Extract domain

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(extracted_domains))

    print(f"Extracted {len(extracted_domains)} domains to {output_file}")

# Input and output file paths

for hosts_file in os.listdir('../raw/blocklist/hosts'):
    input_file = f'../raw/blocklist/hosts/{hosts_file}'
    output_file = f'../processed/blocklist/domains_only_{hosts_file}.txt'
    extract_domains(input_file, output_file)

# for hosts_file in os.listdir('../raw/allowlist/hosts'):
#     input_file = f'../raw/allowlist/hosts/{hosts_file}'
#     output_file = f'../processed/allowlist/domains_only_{hosts_file}.txt'
#     extract_domains(input_file, output_file)