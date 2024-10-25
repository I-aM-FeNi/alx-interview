#!/usr/bin/python3
"""
Log Metrics Processor

This script processes log entries from stdin and computes various metrics.
It handles both continuous processing and graceful interruption via CTRL+C.

Input Format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Example: 127.0.0.1 - [2024-01-01] "GET /projects/260 HTTP/1.1" 200 2000

Features:
    - Processes log entries line by line from stdin
    - Computes total file size
    - Tracks frequency of valid HTTP status codes
    - Prints statistics every 10 lines and on CTRL+C
    - Skips malformed lines
    - Handles graceful shutdown

Valid Status Codes: 200, 301, 400, 401, 403, 404, 405, 500

Usage:
    $ cat logfile.txt | python3 script.py
    or
    $ python3 script.py < logfile.txt
    or
    $ python3 script.py  # Then type/paste log entries manually
"""


import sys

# store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the status code receive exists in the dictionary and
            # increment its count
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # update total size
            total_size += file_size

            # update count of lines
            count += 1

        if count == 10:
            count = 0  # reset count
            print('File size: {}'.format(total_size))

            # print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
