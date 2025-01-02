import pandas as pd
import os
import sys

def calculate_consistency(input_csv, output_json):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Debugging: Print column names and data type of 'naive no fsl correctness'
    print("Columns in the DataFrame:", df.columns.tolist())
    print("Data type of 'naive no fsl correctness':", df['naive no fsl correctness'].dtype)

    # Ensure 'original correctness' and 'naive no fsl correctness' are treated as booleans
    df['original correctness'] = df['original correctness'].astype(bool)
    df['naive no fsl correctness'] = df['naive no fsl correctness'].astype(bool)
    df['naive correctness'] = df['naive correctness'].astype(bool)

    # Add a column to mark correct and incorrect responses
    df['is_correct_no_fsl'] = df['original correctness'] == df['naive no fsl correctness']
    df['is_correct_fsl'] = df['original correctness'] == df['naive correctness']

    # Grouping by 'unique_id'
    grouped = df.groupby('unique_id')

    # Function to calculate consistency for a specific column
    def calculate_group_consistency(group, column):
        # Ensure the group contains the column
        if column not in group.columns:
            raise KeyError(f"'{column}' column is missing in the group.")

        # Calculate the most common value's count and consistency
        most_common_value_count = group[column].value_counts().max()
        total_count = len(group)
        return most_common_value_count / total_count

    # Calculate consistency for each group and store it in a list
    consistencies = []
    for unique_id, group in grouped:
        group_consistency_no_fsl = calculate_group_consistency(group, 'naive no fsl correctness')

        group_consistency_fsl = calculate_group_consistency(group, 'naive correctness')
        group_consistency = (group_consistency_no_fsl + group_consistency_fsl) / 2
        consistencies.append({
            "unique_id": unique_id,
            "consistency_no_fsl": group_consistency_no_fsl,
            "consistency_fsl": group_consistency_fsl,
            "consistency": group_consistency
        })

    # Separate analysis for correct and incorrect responses
    # correct_groups = grouped.filter(lambda x: x['is_correct'].all())
    # incorrect_groups = grouped.filter(lambda x: ~x['is_correct'].all())

    # Define thresholds for majority
    threshold = 0.5  # Majority rule: more than 50% correct responses

    # # Separate analysis for majority-correct and majority-incorrect responses
    # majority_correct_groups = grouped.filter(lambda x: x['is_correct'].mean() > threshold)
    # majority_incorrect_groups = grouped.filter(lambda x: x['is_correct'].mean() <= threshold)


    correct_consistencies = []
    incorrect_consistencies = []

    for unique_id, group in grouped:
        # Calculate the proportion of correct responses
        correct_proportion_no_fsl = group['is_correct_no_fsl'].mean()
        correct_proportion_fsl = group['is_correct_fsl'].mean()
        correct_proportion = (correct_proportion_no_fsl + correct_proportion_fsl) / 2
        # Majority threshold
        threshold = 0.5  # Can be adjusted as needed
        
        if correct_proportion > threshold:
            correct_consistency_no_fsl = calculate_group_consistency(group, 'naive no fsl correctness')
            correct_consistency_fsl = calculate_group_consistency(group, 'naive correctness')
            correct_consistency = (correct_consistency_no_fsl + correct_consistency_fsl) / 2
            # correct_consistency = correct_consistency_fsl
            correct_consistencies.append({
                "unique_id": unique_id,
                "consistency_fsl": correct_consistency_fsl,
                "consistency_no_fsl": correct_consistency_no_fsl,
                "consistency": correct_consistency
            })
        else:  # Majority incorrect or exactly at threshold
            incorrect_consistency_fsl = calculate_group_consistency(group, 'naive no fsl correctness')
            incorrect_consistency_no_fsl = calculate_group_consistency(group, 'naive correctness')
            incorrect_consistency = (incorrect_consistency_no_fsl + incorrect_consistency_fsl) / 2
            # incorrect_consistency =incorrect_consistency_fsl
            incorrect_consistencies.append({
                "unique_id": unique_id,
                "consistency_fsl": incorrect_consistency_fsl,
                "consistency_no_fsl": incorrect_consistency_no_fsl,
                "consistency": incorrect_consistency
            })


    # Calculate average and median consistency for overall, correct, and incorrect responses
    consistency_values = [entry["consistency"] for entry in consistencies]
    correct_values = [entry["consistency"] for entry in correct_consistencies]
    incorrect_values = [entry["consistency"] for entry in incorrect_consistencies]

    average_consistency = sum(consistency_values) / len(consistency_values) if consistency_values else 0
    median_consistency = sorted(consistency_values)[len(consistency_values) // 2] if consistency_values else 0

    average_correct_consistency = sum(correct_values) / len(correct_values) if correct_values else 0
    median_correct_consistency = sorted(correct_values)[len(correct_values) // 2] if correct_values else 0

    average_incorrect_consistency = sum(incorrect_values) / len(incorrect_values) if incorrect_values else 0
    median_incorrect_consistency = sorted(incorrect_values)[len(incorrect_values) // 2] if incorrect_values else 0

    # Prepare results
    results = {
        "group_consistencies": consistencies,
        "correct_consistencies": correct_consistencies,
        "incorrect_consistencies": incorrect_consistencies,
        "summary": {
            "average_consistency": average_consistency,
            "median_consistency": median_consistency,
            "average_correct_consistency": average_correct_consistency,
            "median_correct_consistency": median_correct_consistency,
            "average_incorrect_consistency": average_incorrect_consistency,
            "median_incorrect_consistency": median_incorrect_consistency,
            "total_correct": len(correct_values),
            "total_incorrect": len(incorrect_values)
        }
    }

    # Save results to JSON
    with open(output_json, "w") as json_file:
        import json
        json.dump(results, json_file, indent=4)

    print(f"Results saved to {output_json}")
    print("Consistency Calculations Summary:", results["summary"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <input_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]

    if not os.path.isfile(input_csv):
        print(f"Error: The file '{input_csv}' does not exist.")
        sys.exit(1)

    # Determine the output file path in the same directory as the input CSV
    output_dir = os.path.dirname(input_csv)
    output_json = os.path.join(output_dir, "confidence.json")

    calculate_consistency(input_csv, output_json)
