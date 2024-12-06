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
def analyze_correctness_with_functions(file_path):
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
    
    # Original correlation with number of functions
    for classifier in classifiers:
        comparison_col = f"naive_no_fsl_vs_{classifier}"
        comparison_col_correct_name = f"naive_no_fsl_vs_{correct_names[classifier]}"
        correlation = valid_df[[comparison_col, 'functions']].corr().iloc[0, 1]
        correlation_results[comparison_col_correct_name] = correlation

    # Add `functions_small` boolean column
    valid_df['functions_small'] = valid_df['functions'].apply(lambda x: x <= 1)
    
    # Correlation with `functions_small`
    for classifier in classifiers:
        comparison_col = f"naive_no_fsl_vs_{classifier}"
        comparison_col_correct_name = f"naive_no_fsl_vs_{correct_names[classifier]}_functions_small"
        correlation = valid_df[[comparison_col, 'functions_small']].corr().iloc[0, 1]
        correlation_results[comparison_col_correct_name] = correlation

    # Save results to CSV
    output_folder = os.path.dirname(file_path)
    output_file = os.path.join(output_folder, "functions_analysis_results.csv")
    results_df = pd.DataFrame.from_dict(correlation_results, orient='index', columns=['correlation'])
    results_df.to_csv(output_file, index_label="comparison")

    print(f"Analysis results saved to {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    analyze_correctness_with_functions(input_file)

# Positive Correlation:

# What it means: As the number of functions increases, the naive_no_fsl classifier's relative performance tends to improve compared to the other classifier.
# For example, if the correlation is 0.5, then higher functions numbers are moderately associated with better relative performance of naive_no_fsl.
# Negative Correlation:

# What it means: As the number of functions increases, the naive_no_fsl classifier's relative performance tends to worsen compared to the other classifier.
# For instance, if the correlation is -0.3, higher functions numbers are weakly associated with worse relative performance of naive_no_fsl.

# Positive Correlation 

# What it means: When functions_small is True (functions ≤ 1), the performance of naive_no_fsl relative to the other classifier tends to increase (though slightly in this case).
# Magnitude matters: A small value (like 0.0325) means this effect is very weak, almost negligible. Larger values (closer to 1) would suggest a stronger relationship.
# Negative Correlation 

# What it means: When functions_small is True, the performance of naive_no_fsl relative to the other classifier tends to decrease.
# Magnitude matters: A small negative value (like -0.0162) suggests a very weak relationship. A value closer to -1 would indicate a stronger inverse relationship.