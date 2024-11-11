import pandas as pd

# Specify the paths of the input CSV files
csv_file1 = '/home/jim/HoarePrompt-data/combined_output_apps_4mini_1csv'
csv_file2 = '/home/jim/HoarePrompt-data/combined_output_apps_4mini_2.csv'
# csv_file3 = '/home/jim/HoarePrompt-data/combined_output_apps_3point5_3.csv'

# Specify the path of the output CSV file
output_csv = '/home/jim/HoarePrompt-data/combined_output_apps_4mini_total_runs.csv'

# Read each CSV file into a DataFrame
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
# df3 = pd.read_csv(csv_file3)

# Concatenate the DataFrames
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Save the concatenated DataFrame to the output CSV
concatenated_df.to_csv(output_csv, index=False)

print(f'CSV files have been concatenated and saved to {output_csv}')
