import json
import pandas as pd
import sys

# Check for the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <path_to_json_file>")
    sys.exit(1)

json_path = sys.argv[1]

# Load JSON data from the provided path
with open(json_path, 'r') as file:
    json_data = json.load(file)

# Filter out FSL classifiers
filtered_data = {k: v for k, v in json_data.items() if 'fsl' not in k and 'total_valid_rows' not in k}

# Create a DataFrame
df = pd.DataFrame(filtered_data).T

# Drop the 'description' column
df = df.drop(columns=['description','accuracy', 'precision','agreement_count', 'recall', "f1_score"])

# Convert all columns to numeric for formatting
df = df.apply(pd.to_numeric, errors='ignore')

# Format floating-point numbers
pd.options.display.float_format = '{:.4f}'.format

# Print the table
print(df)
