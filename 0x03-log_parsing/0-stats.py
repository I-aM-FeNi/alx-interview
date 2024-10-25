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
import signal
import re
from collections import defaultdict
from typing import Match, Optional, Dict, Set


class LogProcessor:
    """
    Processes log entries and computes metrics including total file size
    and status code frequencies.

    Attributes:
        l_format (str): Regular expression pattern for valid log entries
        pattern (re.Pattern): Compiled regular expression for log validation
        total_size (int): Running sum of all file sizes
        status_codes (defaultdict): Counter for each status code
        line_count (int): Total number of valid lines processed
        valid_codes (set): Set of valid HTTP status codes to track
        should_exit (bool): Flag for graceful shutdown
    """

    def __init__(self) -> None:
        """
        Initialize the LogProcessor with default values
        and set up signal handling.
        """
        # Regular expression for log line validation and parsing
        self.l_format: str = (
            r'([\d\.]+)\s+-\s+'
            r'\[(.*?)\]\s+'
            r'"GET /projects/260 '
            r'HTTP/1\.1"\s+'
            r'(\d+)\s+'
            r'(\d+)'
            )
        self.pattern = re.compile(self.l_format)

        # Metrics storage
        self.total_size: int = 0
        self.status_codes: Dict[int, int] = defaultdict(int)
        self.line_count: int = 0

        # Valid status codes
        self.valid_codes: Set[int] = {200, 301, 400, 401, 403, 404, 405, 500}

        # Flag for graceful shutdown
        self.should_exit: bool = False

        # Set up signal handler
        signal.signal(signal.SIGINT, self.handle_interrupt)

    def handle_interrupt(self, signum: int, frame: Optional[object]) -> None:
        """
        Handle keyboard interruption (CTRL+C) by printing final statistics
        and performing graceful shutdown.

        Args:
            signum: Signal number
            frame: Current stack frame (not used)
        """
        self.should_exit = True
        self.print_stats()
        sys.exit(0)

    def process_line(self, line: str) -> None:
        """
        Process a single log line, updating metrics if the line is valid.

        The line is considered valid if it:
        1. Matches the expected log format
        2. Contains a valid integer status code
        3. Contains a valid integer file size

        Args:
            line: A single log entry to process
        """
        match: Optional[Match] = self.pattern.match(line.strip())
        if match:
            try:
                # Extract status code and file size
                status_code: int = int(match.group(3))
                file_size: int = int(match.group(4))

                # Update metrics
                if status_code in self.valid_codes:
                    self.status_codes[status_code] += 1
                self.total_size += file_size
                self.line_count += 1

                # Print stats every 10 lines
                if self.line_count % 10 == 0:
                    self.print_stats()

            except ValueError:
                # Skip line if status code or file size is not a valid integer
                pass

    def print_stats(self) -> None:
        """
        Print current statistics including total
        file size and status code counts.

        Statistics are printed in the following format:
        File size: <total_size>
        <status_code>: <count>
        ...

        Status codes are printed in ascending order
        and only if they have occurred
        at least once.
        """
        print(f"\nFile size: {self.total_size}")

        # Print status codes in ascending order
        for code in sorted(self.status_codes.keys()):
            if self.status_codes[code] > 0:
                print(f"{code}: {self.status_codes[code]}")


def main() -> None:
    """
    Main entry point for the log processor.

    Creates a LogProcessor instance and processes stdin line by line
    until EOF or keyboard interruption.
    """
    processor = LogProcessor()

    try:
        for line in sys.stdin:
            processor.process_line(line)
            if processor.should_exit:
                break
    except KeyboardInterrupt:
        # This shouldn't be needed due to signal handler, but just in case
        processor.print_stats()
        sys.exit(0)


if __name__ == "__main__":
    main()

