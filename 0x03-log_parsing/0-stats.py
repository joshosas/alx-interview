#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics:
   Total File Size and Number of lines by status code
'''
import re


def extract_line_input(line_input):
    '''function extracts sections of a line of an HTTP request log.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    req_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    response_match = re.fullmatch(log_format, line_input)
    if response_match is not None:
        status_code = response_match.group('status_code')
        file_size = int(response_match.group('file_size'))
        req_info['status_code'] = status_code
        req_info['file_size'] = file_size
    return req_info


def print_stats(total_file_size, status_codes_stats):
    '''Prints the computed stats of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_req_info = extract_line_input(line)
    status_code = line_req_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_req_info['file_size']


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
