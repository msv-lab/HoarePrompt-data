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

    # Add a column to mark correct and incorrect responses
    df['is_correct'] = df['original correctness'] == df['naive no fsl correctness']

    # Ensure 'logprobs' column is present and numeric
    if 'logprobs' not in df.columns:
        raise KeyError("'logprobs' column is missing in the input CSV.")
    df['logprobs'] = pd.to_numeric(df['logprobs'], errors='coerce').fillna(0)

    # Grouping by 'unique_id'
    grouped = df.groupby('unique_id')

    # Function to calculate new consistency score
    def calculate_group_consistency(group, column, weights_column):
        # Determine the majority response
        majority_response = group[column].mode()[0]

        # Initialize the sum
        weighted_sum = 0
        most_common_value_count = group[column].value_counts().max()
        total_count = len(group)
        consistnecy_old= most_common_value_count / total_count


        # Iterate through rows to calculate the weighted sum
        for _, row in group.iterrows():
            if row[column] == majority_response:
                weighted_sum += row[weights_column]  # Add logprobs for majority response
            else:
                weighted_sum -= row[weights_column]  # Subtract logprobs for non-majority response

        # Calculate consistency score
        num_rows = len(group)
        consistency_score = weighted_sum / num_rows if num_rows > 0 else 0
        return consistency_score, consistnecy_old

    # Calculate consistency for each group
    consistencies = []
    correct_consistencies = []
    incorrect_consistencies = []

    for unique_id, group in grouped:
        # Calculate overall group consistency
        group_consistency, group_consistency_old = calculate_group_consistency(group, 'naive no fsl correctness', 'logprobs')
        consistencies.append({
            "unique_id": unique_id,
            "consistency": group_consistency,
            "consistency_old": group_consistency_old
        })

        # Separate analysis for correct and incorrect groups
        correct_proportion = group['is_correct'].mean()
        threshold = 0.5  # Majority rule: more than 50% correct responses

        if correct_proportion > threshold:
            correct_consistency, correct_consistency_old = calculate_group_consistency(group, 'naive no fsl correctness', 'logprobs')
            correct_consistencies.append({
                "unique_id": unique_id,
                "consistency": correct_consistency,
                "consistency_old": correct_consistency_old
            })
        else:
            incorrect_consistency , incorrect_consistency_old = calculate_group_consistency(group, 'naive no fsl correctness', 'logprobs')
            incorrect_consistencies.append({
                "unique_id": unique_id,
                "consistency": incorrect_consistency,
                "consistency_old": incorrect_consistency_old    
            })

    # Calculate average and median consistency for overall, correct, and incorrect responses
    consistency_values = [entry["consistency"] for entry in consistencies]
    correct_values = [entry["consistency"] for entry in correct_consistencies]
    incorrect_values = [entry["consistency"] for entry in incorrect_consistencies]

    consistency_values_old = [entry["consistency_old"] for entry in consistencies]
    correct_values_old = [entry["consistency_old"] for entry in correct_consistencies]
    incorrect_values_old = [entry["consistency_old"] for entry in incorrect_consistencies]

    average_consistency_old = sum(consistency_values_old) / len(consistency_values_old) if consistency_values_old else 0
    median_consistency_old = sorted(consistency_values_old)[len(consistency_values_old) // 2] if consistency_values_old else 0
    
    average_correct_consistency_old = sum(correct_values_old) / len(correct_values_old) if correct_values_old else 0
    median_correct_consistency_old = sorted(correct_values_old)[len(correct_values_old) // 2] if correct_values_old else 0

    average_incorrect_consistency_old = sum(incorrect_values_old) / len(incorrect_values_old) if incorrect_values_old else 0
    median_incorrect_consistency_old = sorted(incorrect_values_old)[len(incorrect_values_old) // 2] if incorrect_values_old else 0

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
            "average_consistency_old": average_consistency_old,
            "median_consistency_old": median_consistency_old,
            "average_correct_consistency_old": average_correct_consistency_old,
            "median_correct_consistency_old": median_correct_consistency_old,
            "average_incorrect_consistency_old": average_incorrect_consistency_old,
            "median_incorrect_consistency_old": median_incorrect_consistency_old,
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

# Test the function with an example CSV
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
    output_json = os.path.join(output_dir, "confidence_new_metric.json")

    calculate_consistency(input_csv, output_json)