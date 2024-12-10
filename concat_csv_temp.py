import pandas as pd

# Specify the paths of the input CSV files
csv_file1 = '/home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot7/apps_4_mini_2/20241210-165626/20241210-165626.csv'
csv_file2 = '/home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot7/apps_4_mini_1/20241210-131632/20241210-131632.csv'
# csv_file3 = '/home/jim/HoarePrompt-data/Results/Pilot_new5/apps/apps_4_mini_3/20241207-010631/augmented.csv'
# csv_file3 = '/home/jim/HoarePrompt-data/Results/Pilot_new5/mbpp/mbpp_4_mini_3/20241209-224858/augmented.csv'
# csv_file5 = '/home/jim/HoarePrompt-data/Results/Pilot_new2/apps_4_mini_5/combined_apps_4_mini_5.csv'
# csv_file3 = '/home/jim/HoarePrompt-data/combined_output_apps_3point5_3.csv'

# Specify the path of the output CSV file
output_csv = '/home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot7/apps_4_mini_1/20241210-131632/confidence.csv'

# Read each CSV file into a DataFrame
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
# df3 = pd.read_csv(csv_file3)
# df4 = pd.read_csv(csv_file4)
# df5 = pd.read_csv(csv_file5)
# df3 = pd.read_csv(csv_file3)

# Concatenate the DataFrames
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Save the concatenated DataFrame to the output CSV
concatenated_df.to_csv(output_csv, index=False)

print(f'CSV files have been concatenated and saved to {output_csv}')
