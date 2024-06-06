import re
from datetime import datetime


def format_date_string(result):
    # Format date string to DD-MM-YYYY HH:MM:SS format
    return datetime.strptime(result, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')


def format_duration(result):
    # Format duration string to HH:MM:SS format
    result = result[1:]

    hours = 0
    minutes = 0
    seconds = 0

    current_number = ''

    for char in result:
        if char.isdigit():
            current_number += char
        else:
            if char == 'H':
                hours = int(current_number)
            elif char == 'M':
                minutes = int(current_number)
            elif char == 'S':
                seconds = int(current_number)
            current_number = ''

    # Format to hh:mm:ss
    return f"{hours:02}:{minutes:02}:{seconds:02}"
