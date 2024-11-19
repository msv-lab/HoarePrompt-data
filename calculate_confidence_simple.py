import pandas as pd

def calculate_consistency(input_csv, output_json):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Debugging: Print column names and data type of 'naive no fsl correctness'
    print("Columns in the DataFrame:", df.columns.tolist())
    print("Data type of 'naive no fsl correctness':", df['naive no fsl correctness'].dtype)

    # Grouping by 'unique_id'
    grouped = df.groupby('unique_id')

    # Function to calculate consistency for 'naive no fsl correctness'
    def calculate_group_consistency(group):
        # Ensure the group contains the column
        if 'naive no fsl correctness' not in group.columns:
            raise KeyError("'naive no fsl correctness' column is missing in the group.")
        
        # Calculate the most common value's count and consistency
        most_common_value_count = group['naive no fsl correctness'].value_counts().max()
        total_count = len(group)
        return most_common_value_count / total_count

    # Calculate consistency for each group and store it in a list
    consistencies = []
    for unique_id, group in grouped:
        consistency = calculate_group_consistency(group)
        consistencies.append({
            "unique_id": unique_id,
            "consistency": consistency
        })

    # Calculate average and median consistency
    consistency_values = [entry["consistency"] for entry in consistencies]
    average_consistency = sum(consistency_values) / len(consistency_values)
    median_consistency = sorted(consistency_values)[len(consistency_values) // 2]

    # Prepare results
    results = {
        "group_consistencies": consistencies,
        "summary": {
            "average_consistency": average_consistency,
            "median_consistency": median_consistency
        }
    }

    # Save results to JSON
    with open(output_json, "w") as json_file:
        import json
        json.dump(results, json_file, indent=4)

    print(f"Results saved to {output_json}")
    print("Consistency Calculations Summary:", results["summary"])

# Test the function with an example CSV
if __name__ == "__main__":
    input_csv = "/home/jim/HoarePrompt-data/Results/Pilot_confidence_simple/mbpp_4_mini_2/combined_confidence_mbpp_4mini.csv"  # Replace with your input CSV file
    output_json = "confidence.json"  # Desired output JSON file
    calculate_consistency(input_csv, output_json)
