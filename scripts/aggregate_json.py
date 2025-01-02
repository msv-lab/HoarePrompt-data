import json

# Specify the paths of the input JSON files
json_file1 = '/home/jim/HoarePrompt-data/Results/Pilot_reruns/apps_4_mini_1/analysis_report.json'
json_file2 = '/home/jim/HoarePrompt-data/Results/Pilot_reruns/apps_4_mini_2/analysis_report.json'
# json_file3 = '/home/jim/HoarePrompt-data/Results/Pilot_reruns/apps_3point5_3/analysis_report.json'

# Specify the path of the output JSON file
output_json = '/home/jim/HoarePrompt-data/analysis_report_total_4_mini_avg.json'

# Load each JSON file
with open(json_file1) as f:
    data1 = json.load(f)

with open(json_file2) as f:
    data2 = json.load(f)

# with open(json_file3) as f:
#     data3 = json.load(f)

# Initialize a dictionary to store the sum of values and a count of occurrences
summed_data = {}
count_data = {}

# Function to recursively update sums and counts
def update_sums_and_counts(d, summed, count):
    for key, value in d.items():
        if isinstance(value, dict):
            # If the value is a dictionary, recursively call the function
            if key not in summed:
                summed[key] = {}
                count[key] = {}
            update_sums_and_counts(value, summed[key], count[key])
        elif isinstance(value, (int, float)):
            # If the value is a number, update the sum and count
            if key not in summed:
                summed[key] = 0
                count[key] = 0
            summed[key] += value
            count[key] += 1
        else:
            # If the value is not a number (e.g., string), just copy it once
            if key not in summed:
                summed[key] = value

# Update the sums and counts using each input JSON
update_sums_and_counts(data1, summed_data, count_data)
update_sums_and_counts(data2, summed_data, count_data)
# update_sums_and_counts(data3, summed_data, count_data)

# Function to calculate averages from summed data
def calculate_averages(summed, count):
    averaged_data = {}
    for key, value in summed.items():
        if isinstance(value, dict):
            # If the value is a dictionary, recursively calculate averages
            averaged_data[key] = calculate_averages(value, count[key])
        elif isinstance(value, (int, float)):
            # Calculate the average for numerical values
            averaged_data[key] = value / count[key]
        else:
            # Non-numerical values remain the same
            averaged_data[key] = value
    return averaged_data

# Calculate the average data structure
average_data = calculate_averages(summed_data, count_data)

# Save the averaged data to the output JSON file
with open(output_json, 'w') as f:
    json.dump(average_data, f, indent=4)

print(f'Averages calculated and saved to {output_json}')
