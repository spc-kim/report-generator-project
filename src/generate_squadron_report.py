"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.

    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    # Read and load pilots CSV:
    pilots_filepath = '../data/pilots.csv'
    pilots = rf.read_csv_file(pilots_filepath)
    print(pilots[0])
    # Read and load flight logs CSV:
    flight_logs_filepath = '../data/flight_logs.csv'
    flight_logs = rf.read_csv_file(flight_logs_filepath)
    print(flight_logs[0])
    # Read and load aircraft CSV:
    aircraft_filepath = '../data/aircraft.csv'
    aircraft = rf.read_csv_file(aircraft_filepath)
    print(aircraft[0])

    # TODO: PART 2 - Filter data for the specified squadron
    # Filter out pilots not belonging to specified squadron:
    squadron_pilots = rf.filter_by_field(pilots, 'squadron', squadron_code)
    print(squadron_pilots[0])
    # Filter out aircraft not belonging to specified squadron:
    squadron_aircraft = rf.filter_by_field(aircraft, 'squadron', squadron_code)
    print(squadron_aircraft[0])

    # TODO: PART 3 - Get flights for squadron pilots
    # Join pilots list with flight logs with pilot data by the shared pilot id column
    joined_flight_logs = rf.join_data(flight_logs, pilots, 'pilot_id', 'pilot_id')
    print(joined_flight_logs[0])
    # Filter out joined flight logs that don't have matching squadron
    squadron_flight_logs = rf.filter_by_field(joined_flight_logs, 'squadron', squadron_code)
    print(squadron_flight_logs[0])

    # TODO: PART 4 - Calculate statistics
    # Total flight hours for the squadron
    squadron_total_hours = rf.calculate_total(squadron_flight_logs, 'duration_hours')
    print(squadron_total_hours)
    # Total number of missions flown
    squadron_total_missions = rf.count_records(squadron_flight_logs)
    print(squadron_total_missions)
    # Breakdown of missions by type (Training, Patrol, Combat, etc.)
    squadron_mission_types = rf.get_unique_values(squadron_flight_logs, 'mission_type')
    print(squadron_mission_types)
    # Average mission duration
    squadron_avg_mission_duration = rf.calculate_average(squadron_flight_logs, 'duration_hours')
    print(squadron_avg_mission_duration)

    # TODO: PART 5 - Build the report content
    pass

    # TODO: PART 6 - Write the report to file
    pass


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")

    # print("\nImplement the function above, then uncomment to test!")

    # Example: Generate report for VFA-41 (Black Aces)
    generate_squadron_report('VFA-41', '../reports/vfa-41-report.txt')