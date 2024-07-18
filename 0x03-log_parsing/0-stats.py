#!/usr/bin/python3
import sys
import signal
import re

total_file_size = 0
status_codes_count = {}
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

def print_stats():
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        match = re.match(r"^(\S+) - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$", line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            
            total_file_size += file_size
            
            if status_code in valid_status_codes:
                if status_code not in status_codes_count:
                    status_codes_count[status_code] = 0
                status_codes_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    pass
finally:
    print_stats()
