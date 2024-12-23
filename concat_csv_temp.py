import pandas as pd

# Specify the paths of the input CSV files
csv_file1 = '/home/jim/HoarePrompt-data/Results/Pilot_new11/apps_llama_1/20241218-235125/20241218-235125.csv'
csv_file2 = '/home/jim/HoarePrompt-data/Results/Pilot_new11/apps_llama_2/20241220-181418/20241220-181418.csv'
# csv_file3 = '/home/jim/HoarePrompt-data/Results/Pilot_new11/apps_llama_3/20241221-154729/20241221-154729.csv'
csv_file4 = '/home/jim/HoarePrompt-data/Results/Pilot_new11/hoareprompt_data_temp/APPS_REMOTE_LLAMA_!/20241218-104323.csv'
# csv_file5 = '/home/jim/HoarePrompt-data/Results/Pilot_new2/apps_4_mini_5/combined_apps_4_mini_5.csv'
# csv_file3 = '/home/jim/HoarePrompt-data/combined_output_apps_3point5_3.csv'

# Specify the path of the output CSV file
output_csv = '/home/jim/HoarePrompt-data/Results/Pilot_new11/APPS_llama_FINAL/output.csv'

# Read each CSV file into a DataFrame
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
# df3 = pd.read_csv(csv_file3)
df4 = pd.read_csv(csv_file4)
# df5 = pd.read_csv(csv_file5)
# df3 = pd.read_csv(csv_file3)

# Concatenate the DataFrames
concatenated_df = pd.concat([df1, df2,df4], ignore_index=True)

# Save the concatenated DataFrame to the output CSV
concatenated_df.to_csv(output_csv, index=False)

print(f'CSV files have been concatenated and saved to {output_csv}')
