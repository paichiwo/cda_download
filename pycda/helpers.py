from datetime import datetime


def format_date_string(result):
    # Format date string to DD-MM-YYYY HH:MM:SS format
    return datetime.strptime(result, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
