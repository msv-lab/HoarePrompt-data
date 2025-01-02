import os
import pandas as pd
import json

def process_csv(file_path):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Ensure columns exist
        required_columns = ['confidence1', 'confidence2']
        for col in required_columns:
            if col not in data.columns:
                raise KeyError(f"Missing required column: {col}")

        # Convert columns to numeric, coercing errors to NaN
        for col in required_columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')

        # Calculate average and median, skipping NaN
        results = {}
        for col in required_columns:
            if data[col].isna().all():
                print(f"All values in column '{col}' are invalid or missing.")
                results[col] = {"average": None, "median": None}
            else:
                avg = data[col].mean()
                median = data[col].median()
                results[col] = {"average": avg, "median": median}

        # Create the output JSON file path
        output_dir = os.path.dirname(file_path)
        output_file = os.path.join(output_dir, "results.json")

        # Write results to a JSON file
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=4)

        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error processing file: {e}")

# File path to your CSV
input_csv = "/home/jim/HoarePrompt-data/Results/Pilot_confidence/mbpp_3point5_2/combined_confidence_mbpp_3point5.csv"  # Replace with the path to your CSV file

# Call the function
process_csv(input_csv)
