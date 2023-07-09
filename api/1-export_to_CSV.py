#!/usr/bin/python3
"""import module and export data to  csv"""
import csv
if __name__ == '__name__':

    # Specify the CSV file name based on the employee ID
    csv_filename = "{}.csv".format(EMPLOYEE_ID)

    # Export data to CSV
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Write the header row

        for task in data:
            writer.writerow([EMPLOYEE_ID, EMPLOYEE_NAME, str(task["completed"]), task["title"]])  # Write each task as a row in CSV
