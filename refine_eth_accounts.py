#!/usr/bin/env python3
"""
Check the list of input strings from STDIN to comply ethereum account format (42-digit hex string starting with '0x').
Remove duplicates and sort items alphabetically.
Print refined list to STDOUT.
"""
import re
import sys

refined_addresses = []

for input_line in sys.stdin:
    line = input_line.strip()
    # Try to match Ethereum address regexp
    m = re.match(r"^0x[a-fA-F0-9]{40}$", line)
    if m:
        refined_addresses.append(line)
    else:
        print(f"Regex not matched {line}", file=sys.stderr)

# remove duplicates
refined_addresses = sorted(set(refined_addresses))
for addr in refined_addresses:
    print(addr)
