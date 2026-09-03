"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv


def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # TODO: Your code here
    # Hint: Use csv.DictReader to read CSV files into dictionaries
    # Hint: Remember to use 'with open()' for proper file handling
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def count_records(data_list):
    """Counts the number of records in a dataset."""
    # TODO: Your code here
    # Hint: Use the len() function
    records = len(data_list)
    return records


def get_unique_values(data_list, field_name):
    """Gets all unique values for a specific field in the dataset."""
    # TODO: Your code here
    # Hint: Use a set to collect unique values
    # Hint: Convert the set to a list and sort it before returning
    unique_set = set()
    for record in data_list:
        value = record[field_name]
        unique_set.add(value)
    return sorted(list(unique_set))


def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    # TODO: Your code here
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions
    filtered_data_list = []
    for record in data_list:
        if record[field_name] == field_value:
            filtered_data_list.append(record)
    return filtered_data_list


def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    # Hint: Initialize a total variable to 0
    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!
    total = 0.0
    for record in data_list:
        value_to_add = float(record[field_name])
        total += value_to_add
    return total


def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    # Hint: Use calculate_total() and count_records() functions
    # Hint: Average = total / count
    count = count_records(data_list)
    if count == 0:
        return 0.0
    total = calculate_total(data_list, field_name)
    average = total / count
    return average


def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # TODO: Your code here
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value
    for record in data_list:
        if record[id_field] == id_value:
            return record


def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    # Hint: For each record in primary_list, look up the matching secondary record
    # Hint: Use dict.update() to merge dictionaries
    pass


def write_report_to_file(filepath, content):
    """Writes a text report to a file."""
    # TODO: Your code here
    # Hint: Use 'with open(filepath, 'w')' to open file for writing
    pass


def format_header(title):
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    # Hint: Use .center(60) to center the title
    pass


# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")
    print("Implement functions above, then uncomment test code below")

    # read_csv_file(filepath):
    pilots = read_csv_file('../data/pilots.csv')
    print(f"Loaded {len(pilots)} pilots")

    print(f"First pilot entry: {pilots[0]}")

    # count_records(data_list):
    pilots_count = count_records(pilots)
    print(f"Pilots count: {pilots_count}")

    # get_unique_values(data_list, field_name):
    pilots_ranks = get_unique_values(pilots, 'rank')
    print(f"Pilots ranks: {pilots_ranks}")

    # filter_by_field(data_list, field_name, field_value):
    pilots_rank_filtered = filter_by_field(pilots, 'rank', 'Lt')
    print(f"Pilots ranks filtered by Lt: {pilots_rank_filtered}")

    # calculate_total(data_list, field_name):
    pilots_total_flight_hours = calculate_total(pilots, 'total_flight_hours')
    print(f"Pilots total flight hours: {pilots_total_flight_hours}")

    # calculate_average(data_list, field_name):
    pilots_average_flight_hours = calculate_average(pilots, 'total_flight_hours')
    print(f"Pilots average flight hours: {pilots_average_flight_hours}")

    # find_record_by_id(data_list, id_field, id_value):
    pilots_twentieth_id = find_record_by_id(pilots, 'pilot_id', 'P020')
    print(f"Pilots 20th ID: {pilots_twentieth_id}")