import pandas as pd
import numpy as np
import sys
import os

# Helper functions for metrics
def calculate_agreement(df, col1, col2):
    agreement = (df[col1] == df[col2]).sum()
    percentage = agreement / len(df) * 100
    return agreement, percentage

def calculate_confusion_matrix(df, truth_col, pred_col):
    tp = ((df[truth_col] == True) & (df[pred_col] == True)).sum()
    tn = ((df[truth_col] == False) & (df[pred_col] == False)).sum()
    fp = ((df[truth_col] == False) & (df[pred_col] == True)).sum()
    fn = ((df[truth_col] == True) & (df[pred_col] == False)).sum()
    return tp, tn, fp, fn

def calculate_mcc(tp, tn, fp, fn):
    numerator = (tp * tn) - (fp * fn)
    denominator = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return numerator / denominator if denominator != 0 else 0

def calculate_accuracy(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) != 0 else 0

def calculate_precision(tp, fp):
    return tp / (tp + fp) if (tp + fp) != 0 else 0

def calculate_recall(tp, fn):
    return tp / (tp + fn) if (tp + fn) != 0 else 0

def calculate_f1_score(tp, fp, fn):
    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)
    return 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

def calculate_balanced_accuracy(tp, tn, fp, fn):
    sensitivity = calculate_recall(tp, fn)
    specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
    return (sensitivity + specificity) / 2

# Main analysis function
def analyze_correctness_with_consistency(file_path):
    # Load CSV and preprocess
    df = pd.read_csv(file_path)
    columns_to_preprocess = ['Correctness', 'naive correctness', 'original correctness', 
                             'annotated correctness', 'annotated correctness simple', 
                             'naive no fsl correctness']
    valid_df = df.dropna(subset=columns_to_preprocess)

    # Initialize comparison variables
    classifiers = ['Correctness', 'naive correctness', 'annotated correctness', 'annotated correctness simple']
    for classifier in classifiers:
        comparison_col = f"naive_no_fsl_vs_{classifier}"
        valid_df[comparison_col] = 0

    # Calculate comparison variables
    for index, row in valid_df.iterrows():
        naive_correct = row['naive no fsl correctness'] == row['original correctness']
        for classifier in classifiers:
            classifier_correct = row[classifier] == row['original correctness']
            comparison_col = f"naive_no_fsl_vs_{classifier}"
            if naive_correct and not classifier_correct:
                valid_df.at[index, comparison_col] = 1
            elif not naive_correct and classifier_correct:
                valid_df.at[index, comparison_col] = -1
            else:
                valid_df.at[index, comparison_col] = 0

    # Correlation analysis
    correlation_results = {}
    correct_names = {"Correctness": "Function summary", "naive correctness": "Naive", "annotated correctness": "Complex tree", "annotated correctness simple": "Simple tree", "naive no fsl correctness": "Naive No FSL"}
    for classifier in classifiers:
        comparison_col = f"naive_no_fsl_vs_{classifier}"
        comparison_col_correct_name = f"naive_no_fsl_vs_{correct_names[classifier]}"
        correlation = valid_df[[comparison_col, 'consistency']].corr().iloc[0, 1]
        correlation_results[comparison_col_correct_name] = correlation

    # Save results to CSV
    output_folder = os.path.dirname(file_path)
    output_file = os.path.join(output_folder, "consistency_analysis_results.csv")
    results_df = pd.DataFrame.from_dict(correlation_results, orient='index', columns=['correlation_with_consistency'])
    results_df.to_csv(output_file, index_label="comparison")

    print(f"Analysis results saved to {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    analyze_correctness_with_consistency(input_file)


# A positive correlation means that when consistency is high, naive no FSL correctness tends to perform better relative to the other classifiers.
# A negative correlation means that when consistency is high, naive no FSL correctness tends to perform worse relative to the other classifiers.
# A near-zero correlation means that the relationship between consistency and performance difference is weak or non-existent.
#pearsons correlation