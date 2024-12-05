import pandas as pd
import json
import os
from itertools import combinations

def load_csv(file_path):
    return pd.read_csv(file_path)

def compare_classifiers(df, classifiers, base_truth):
    results = {}
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

        # Calculate statistics for A vs B comparison
        a_outperforms_count = len(a_outperforms_b)
        b_outperforms_count = len(b_outperforms_a)

        avg_consistency_a = sum(item['consistency'] for item in a_outperforms_b) / a_outperforms_count if a_outperforms_count > 0 else 0
        avg_consistency_b = sum(item['consistency'] for item in b_outperforms_a) / b_outperforms_count if b_outperforms_count > 0 else 0

        results[f"{classifier_a}_vs_{classifier_b}"] = {
            f"{classifier_a}_outperforms_{classifier_b}": {
                "rows": a_outperforms_b,
                "count": a_outperforms_count,
                "average_consistency": avg_consistency_a
            },
            f"{classifier_b}_outperforms_{classifier_a}": {
                "rows": b_outperforms_a,
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

    classifiers = [
        'naive no fsl correctness',
        'Correctness', 
        'naive correctness', 
        'annotated correctness', 
        'annotated correctness simple'
        
    ]
    base_truth = 'original correctness'

    results = compare_classifiers(df, classifiers, base_truth)

    output_dir = os.path.dirname(input_csv)
    output_file = os.path.join(output_dir, "classifier_comparison_results.json")
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
