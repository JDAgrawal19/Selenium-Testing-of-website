import csv
from datetime import date,timedelta

def get_csv_data(filename):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    datafile = open(filename, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(datafile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


def get_current_date_with_format_same_as_timesheet():
    today = date.today()
    return today.strftime("%b %d")


def get_date_before_n_number_of_days_with_format_of_timesheet(n):
    today = date.today()
    previous_date = today - timedelta(days=n)
    return previous_date.strftime("%b %d")
