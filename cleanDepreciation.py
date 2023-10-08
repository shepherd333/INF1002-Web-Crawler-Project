import csv


def remove_yr_from_data(input_file, output_file):
    # Read the CSV file and process the data
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Process the row and remove "/yr" from the appropriate column(s)
            processed_row = [cell.replace("/yr", "") if "/yr" in cell else cell for cell in row]
            writer.writerow(processed_row)


# Replace 'input.csv' with the actual path and filename of your input CSV file
# Replace 'output.csv' with the desired output file path and filename
input_file = 'UsedCars_20sep.csv'
output_file = 'newUsedCars_20sep.csv'

remove_yr_from_data(input_file, output_file)
