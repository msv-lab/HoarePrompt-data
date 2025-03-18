import pandas as pd
import sys
import json
import math

def preprocess_correctness(value, task_id):
    """Normalize correctness values to boolean."""
    normalized_value = str(value).strip().lower()
    if normalized_value in ["correct", "true"]:
        return True
    elif normalized_value in ["incorrect", "false"]:
        return False
    else:
        print(f"Error: Task ID {task_id} has an unrecognized correctness value '{value}'")
        return None

def calculate_mcc(tp, tn, fp, fn):
    """Calculate Matthews correlation coefficient (MCC)."""
    numerator = (tp * tn) - (fp * fn)
    denominator = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return float(numerator / denominator if denominator != 0 else 0)

def calculate_agreement(df, col1, col2):
    """Calculate agreement count between two columns."""
    return int((df[col1] == df[col2]).sum())

def calculate_confusion_matrix(df, col1, col2):
    """Calculate TP, TN, FP, FN between two columns."""
    tp = int(((df[col1] == True) & (df[col2] == True)).sum())
    tn = int(((df[col1] == False) & (df[col2] == False)).sum())
    fp = int(((df[col1] == False) & (df[col2] == True)).sum())
    fn = int(((df[col1] == True) & (df[col2] == False)).sum())
    return tp, tn, fp, fn

def process_correctness_columns(df, columns):
    """Preprocess correctness-related columns."""
    for col in columns:
        df[col] = df.apply(lambda row: preprocess_correctness(row[col], row['Task ID']), axis=1)
    return df.dropna(subset=columns)

def calculate_balanced_accuracy(tp, tn, fp, fn):
    """Calculate balanced accuracy."""
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    return float((sensitivity + specificity) / 2)

def calculate_tpr(tp, fn):
    """Calculate True Positive Rate (TPR)."""
    return float(tp / (tp + fn) if (tp + fn) > 0 else 0)

def calculate_fnr(fn, tp):
    """Calculate False Negative Rate (FNR)."""
    return float(fn / (tp + fn) if (tp + fn) > 0 else 0)

def calculate_fpr(fp, tn):
    """Calculate False Positive Rate (FPR)."""
    return float(fp / (fp + tn) if (fp + tn) > 0 else 0)

def analyze_correctness(file_path, output_json_path):
    df = pd.read_csv(file_path)
    columns_to_preprocess = ["original correctness", "complex tree", "vanilla", "vanilla_no_cot"]
    valid_df = process_correctness_columns(df, columns_to_preprocess)
    
    comparisons = [
        ('complex tree', 'original correctness',  "hoareprompt"),
        ('vanilla', 'original correctness', 'zero_shot_cot'),
        ('vanilla_no_cot', 'original correctness', 'vanilla_no_cot')
    ]
    dict1={'complex tree': "hoareprompt", "vanilla": "zero_shot_cot", "vanilla_no_cot": "vanilla_no_cot"}
    results = {}
    for col1, col2,col3 in comparisons:
        agreement_count = calculate_agreement(valid_df, col1, col2)
        tp, tn, fp, fn = calculate_confusion_matrix(valid_df, col2, col1)
        mcc = calculate_mcc(tp, tn, fp, fn)
        balanced_accuracy = calculate_balanced_accuracy(tp, tn, fp, fn)
        tpr = calculate_tpr(tp, fn)
        fnr = calculate_fnr(fn, tp)
        fpr = calculate_fpr(fp, tn)
        
        results[dict1[col1]] = {
            "Agreement Count": agreement_count,
            "Balanced Accuracy": balanced_accuracy,
            "True Positive Rate (TPR)": tpr,
            "False Negative Rate (FNR)": fnr,
            "False Positive Rate (FPR)": fpr,
            "MCC": mcc
        }
    
    # Ensure JSON serializability by converting NumPy data types to Python native types
    with open(output_json_path, "w") as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python analyze_correctness.py <csv_file_path> <output_json_file_path>")
    else:
        file_path = sys.argv[1]
        output_json_path = sys.argv[2]
        analyze_correctness(file_path, output_json_path)
