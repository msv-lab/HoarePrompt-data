import pandas as pd
import json
import os
from itertools import combinations
from collections import defaultdict

def load_csv(file_path):
    return pd.read_csv(file_path)

def aggregate_results_by_unique_id(rows1, rows2, df):
    """
    Aggregates results by unique_id. Consolidates consistency and count for each unique_id.
    """
    aggregated1 = defaultdict(lambda: {"consistency": 0, "count": 0, "performance": 0})
    aggregated2 = defaultdict(lambda: {"consistency": 0, "count": 0, "performance": 0})

    for row in rows1:
        unique_id = row['unique_id']
        aggregated1[unique_id]["consistency"] += row['consistency']
        aggregated1[unique_id]["count"] += 1
    
    for row in rows2:
        unique_id = row['unique_id']
        aggregated2[unique_id]["consistency"] += row['consistency']
        aggregated2[unique_id]["count"] += 1

    return_list1 = []
    # Normalize consistency (average consistency per occurrence)
    for unique_id, data in aggregated1.items():
        #findin how many rows the unique_id is present in the df
        data["consistency"] = data["consistency"] / data["count"]
        reruns = len(df[df['unique_id'] == unique_id])
        count1= data["count"]
        if unique_id in aggregated2:
            count2 = aggregated2[unique_id]["count"]
        else:
            count2 = 0
        data["performance"] = (count1-count2) / reruns
        return_list1.append({"unique_id": unique_id, "consistency": data["consistency"], "count" :data["count"], "reruns": reruns, "performance": data["performance"]})
    
    return_list2 = []
    # Normalize consistency (average consistency per occurrence)
    for unique_id, data in aggregated2.items():
        #findin how many rows the unique_id is present in the df
        data["consistency"] = data["consistency"] / data["count"]
        reruns = len(df[df['unique_id'] == unique_id])
        count2= data["count"]
        if unique_id in aggregated1:
            count1 = aggregated1[unique_id]["count"]
        else:
            count1 = 0
        data["performance"] = (count2-count1) / reruns
        return_list2.append({"unique_id": unique_id, "consistency": data["consistency"], "count" :data["count"] ,"reruns": reruns, "performance": data["performance"]})
    

    return return_list1, return_list2

def compare_classifiers(df, classifiers, base_truth):
    results = {}
    # correct_names = {"Correctness": "Function summary", "naive correctness": "Naive", "annotated correctness": "Complex tree", "annotated correctness simple": "Simple tree", "naive no fsl correctness": "Vanilla", 'Correctness no fsl': 'Function summary no FSL', 'simple verify': 'Simple verify ', 'complex verify': 'Complex verify', 'default verify': 'Default verify', 'simple verify no fsl': 'Simple verify no FSL', 'complex verify no fsl': 'Complex verify no FSL', 'default verify no fsl': 'Default verify no FSL'}

    for classifier_a, classifier_b in combinations(classifiers, 2):
        a_outperforms_b = []
        b_outperforms_a = []

        for _, row in df.iterrows():
            base_correct = row[base_truth]
            a_correct = row[classifier_a] == base_correct
            b_correct = row[classifier_b] == base_correct

            if a_correct and not b_correct:
                a_outperforms_b.append({"unique_id": row['unique_id'], "consistency": row['consistency']})
            elif b_correct and not a_correct:
                b_outperforms_a.append({"unique_id": row['unique_id'], "consistency": row['consistency']})


        # Aggregate results by unique_id
        aggregated_a_outperforms_b , aggregated_b_outperforms_a= aggregate_results_by_unique_id(a_outperforms_b, b_outperforms_a, df)

        # Calculate statistics for A vs B comparison
        a_outperforms_count = len(aggregated_a_outperforms_b)
        b_outperforms_count = len(aggregated_b_outperforms_a)

        avg_consistency_a = sum(item['consistency'] for item in aggregated_a_outperforms_b) / a_outperforms_count if a_outperforms_count > 0 else 0
        avg_consistency_b = sum(item['consistency'] for item in aggregated_b_outperforms_a) / b_outperforms_count if b_outperforms_count > 0 else 0

        results[f"{classifier_a}_vs_{classifier_b}"] = {
            f"{classifier_a}_outperforms_{classifier_b}": {
                "rows": aggregated_a_outperforms_b,
                "count": a_outperforms_count,
                "average_consistency": avg_consistency_a
            },
            f"{classifier_b}_outperforms_{classifier_a}": {
                "rows": aggregated_b_outperforms_a,
                "count": b_outperforms_count,
                "average_consistency": avg_consistency_b
            }
        }
    return results

def save_results(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

# Main function
def main(input_csv):
    df = load_csv(input_csv)

    classifiers =  [ "naive correctness fsl","vanilla","summary fsl",   "simple tree", "complex tree",  "summary" , "simple verify fsl", "complex verify fsl", "summary verify fsl", "simple verify", "complex verify", "summary verify"]

    base_truth = 'original correctness'

    results = compare_classifiers(df, classifiers, base_truth)

    output_dir = os.path.dirname(input_csv)
    output_file = os.path.join(output_dir, "classifier_comparison_results_naive_fsl.json")
    save_results(results, output_file)

    print(f"Comparison results saved to {output_file}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    main(input_csv)