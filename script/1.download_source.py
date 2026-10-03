#!/usr/bin/env python3
import requests, os

for wh_file in os.listdir('../src/allowlist'):
    if wh_file == 'do_not_download': continue
    allowlist_file = open(f'../src/allowlist/{wh_file}', 'r')
    for a in allowlist_file:
        url = a.strip()  # Remove any leading/trailing whitespace
        filename = url[8:].replace('/', '_')  # Create a safe filename
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            with open(f'../raw/allowlist/{wh_file}/{filename}', 'wb') as file:  # Save content to a file
                file.write(response.content)
            print(f"Downloaded: {url} -> downloads/{filename}")
        except requests.RequestException as e:
            print(f"Failed to download {url}: {e}")

for bl_file in os.listdir('../src/blocklist'):
    if bl_file == 'do_not_download': continue
    blocklist_file = open(f'../src/blocklist/{bl_file}', 'r')
    for b in blocklist_file:
        url = b.strip()  # Remove any leading/trailing whitespace
        filename = url[8:].replace('/', '_')  # Create a safe filename
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            with open(f'../raw/blocklist/{bl_file}/{filename}', 'wb') as file:  # Save content to a file
                file.write(response.content)
            print(f"Downloaded: {url} -> downloads/{filename}")
        except requests.RequestException as e:
            print(f"Failed to download {url}: {e}")