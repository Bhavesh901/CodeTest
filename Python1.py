#Write a Python program to read a CSV file and display its contents.
import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'C:/Users/JB/Downloads/test_file.csv'  # Replace with your CSV file path
read_csv(file_path)

#OUTPUT:
#['Product', 'Region', 'Sales Amount', 'Date']
#['Product A', 'North', '1200', '01-01-2024']
#['Product B', 'South', '1500', '02-01-2024']
#['Product C', 'East', '800', '03-01-2024']
#['Product D', 'West', '700', '04-01-2024']
#['Product A', 'North', '1100', '05-01-2024']
#['Product B', 'South', '1400', '06-01-2024']
#['Product C', 'East', '900', '07-01-2024']
#['Product A', 'North', '1300', '09-01-2024']
#['Product B', 'South', '1600', '10-01-2024']
