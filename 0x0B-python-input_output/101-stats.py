#!/usr/bin/python3
"""
Module contains  a script that reads
stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """
    Prints the statistics based on the total
    file size and status code counts.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary containing
        status code counts.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))


def parse_line(line):
    """
    Parses a line and extracts the status code
    and file size.

    Args:
        line (str): The input line.

    Returns:
        tuple: A tuple containing the status code
        and file size.
    """
    parts = line.strip().split(" ")
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size


def compute_metrics():
    """
    Reads stdin line by line, computes the metrics,
    and prints the statistics.

    Returns:
        None
    """
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    compute_metrics()
