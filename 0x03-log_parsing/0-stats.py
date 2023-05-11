#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics:
   returning Total file size and Number of lines by status code
'''
import sys


status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

for line in sys.stdin:
    # Parse the line using string methods and regular expressions
    match = re.match(
        r'^([\d.]+) - \[(.*)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line.strip())

    if not match:
        continue

    ip_address, date_str, status_code_str, file_size_str = match.groups()
    status_code = int(status_code_str)
    file_size = int(file_size_str)

    total_size += file_size
    status_counts[status_code] += 1

    line_count += 1

    if line_count % 10 == 0 or line_count == sys.maxsize:
        print(f"Total file size: File size: {total_size}")

        for code in sorted(status_counts.keys()):
            count = status_counts[code]
            if count > 0:
                print(f"{code}: {count}")

        status_counts = {200: 0, 301: 0, 400: 0,
                         401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

        line_count = 0
