#!/usr/bin/python3
"""Prints the statistics of the logs"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics of the logs.
    Args:
        total_size (int): The total size of the files.
        status_codes (dict): A dictionary with status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_codes.keys()):
        print("{}: {}".format(status, status_codes[status]))


def process_logs():
    """
    Process log entries from stdin and print statistics.
    """
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                total_size += int(parts[-1])
                if parts[-2] in status_codes:
                    status_codes[parts[-2]] += 1
                else:
                    status_codes[parts[-2]] = 1
            except (ValueError, IndexError):
                pass
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    process_logs()
