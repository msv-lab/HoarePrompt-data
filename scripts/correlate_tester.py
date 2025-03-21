import pandas as pd
import json
import sys
import os
from scipy.stats import pearsonr

def normalize_correctness(val):
    val = str(val).strip().lower()
    if val in ['true', 'correct']:
        return True
    elif val in ['false', 'incorrect']:
        return False
    return None

def compute_correlations(pairs):
    values = [x[0] for x in pairs]
    matches = [x[1] for x in pairs]
    if len(set(values)) <= 1:
        return None
    return pearsonr(values, matches)

def correlate(csv_path, json_path):
    # Load CSV and JSON
    df = pd.read_csv(csv_path)
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    json_dict = {item['unique_id']: item for item in json_data}

    classifiers = ['tester']
    features = ['depth', 'hard', 'LOC']

    # Initialize output structures
    correlations = {clf: {feat: None for feat in features} for clf in classifiers}
    pairs = {clf: {feat: [] for feat in features} for clf in classifiers}

    # Comparative analysis output
    comparative = {feat: {} for feat in features}
  
    # delta_pairs = {feat: {f"{a}_vs_{b}": [] for a, b in classifier_pairs} for feat in features}

    for _, row in df.iterrows():
        uid = row['unique_id']
        if uid not in json_dict:
            continue

        json_entry = json_dict[uid]
        truth = normalize_correctness(row.get('original correctness'))
        if truth is None:
            continue

        match = {}
        for clf in classifiers:
            pred = normalize_correctness(row.get(clf))
            if pred is None:
                continue
            match[clf] = int(pred == truth)
            for feat in features:
                if feat in json_entry:
                    val = json_entry[feat]
                    pairs[clf][feat].append((val, match[clf]))

        # # Comparative correlation: difference in correctness-match
        # for a, b in classifier_pairs:
        #     if a in match and b in match:
        #         diff = match[a] - match[b]
        #         for feat in features:
        #             if feat in json_entry:
        #                 delta_pairs[feat][f"{a}_vs_{b}"].append((json_entry[feat], diff))

    # Compute individual correlations
    for clf in classifiers:
        for feat in features:
            corr_result = compute_correlations(pairs[clf][feat])
            if corr_result:
                corr, p_val = corr_result
                correlations[clf][feat] = {
                    "pearson_correlation": corr,
                    "p_value": p_val,
                    "count": len(pairs[clf][feat])
                }

    # # Compute comparative correlations
    # for feat in features:
    #     for pair_name, data in delta_pairs[feat].items():
    #         if len(set(x[0] for x in data)) > 1:
    #             x = [v[0] for v in data]
    #             y = [v[1] for v in data]
    #             corr, p_val = pearsonr(x, y)
    #             comparative[feat][pair_name] = {
    #                 "delta_correlation": corr,
    #                 "p_value": p_val,
    #                 "count": len(data)
    #             }
    #         else:
    #             comparative[feat][pair_name] = None

    # Final output structure
    final_output = {
        "individual_correlations": correlations
        # "comparative_correlations": comparative
    }

    # Save output
    out_path = os.path.splitext(csv_path)[0] + "_correlations.json"
    with open(out_path, 'w') as f:
        json.dump(final_output, f, indent=4)

    print(f"Correlations saved to: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python correlate_features.py <csv_path> <json_path>")
    else:
        correlate(sys.argv[1], sys.argv[2])
