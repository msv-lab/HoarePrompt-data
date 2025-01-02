# Script: `verify_temp.py`

## Purpose
Processes datasets with precomputed results (`naive`, `naive_no_fsl`, `annotated`) to compute verification metrics (`simple_verify`, `complex_verify`, `default_verify`, and their `no_fsl` variants) without rerunning HoarePrompt.

## Features
- **Parse and Clean Code**:
  - Removes imports and comments.
  - Extracts global code and function definitions.
- **Dataset Processing**:
  - Reads results from `.csv`, `.md`, and `.py` files in a structured dataset directory.
  - Computes verification metrics using existing method outputs.
- **Result Consolidation**:
  - Updates metrics into a DataFrame and exports a new `total_results.csv`.

## Usage
```bash
python verify_temp.py <input_directory>
```

# Script: `qualitative_analysis_naive.py`

## Purpose
Compares the results of the naive method against all other classifiers to:
1. Identify examples where classifiers differ from the naive approach.
2. Calculate **performance** metrics that measure how consistently one classifier outperforms another, ranging from -1 (always outperformed) to 1 (always outperforming).
3. Store consistency values for correlation analysis.

## Features
- **Result Aggregation**:
  - Aggregates differences by `unique_id` and computes consistency, reruns, and performance metrics.
- **Classifier Comparisons**:
  - Compares pairs of classifiers to analyze which one performs better relative to the base truth (`original correctness`).
- **Output Generation**:
  - Saves detailed comparison results, including rows, counts, and average consistency, in a structured JSON file.

## Usage
```bash
python qualitative_analysis_naive.py <path_to_csv>
```


# Script: `qualitative_analysis_naive_no_fsl.py`

## Purpose
Compares the results of the naive no fsl method against all other classifiers to:
1. Identify examples where classifiers differ from the naive no fsl approach.
2. Calculate **performance** metrics that measure how consistently one classifier outperforms another, ranging from -1 (always outperformed) to 1 (always outperforming).
3. Store consistency values for correlation analysis.

## Features
- **Result Aggregation**:
  - Aggregates differences by `unique_id` and computes consistency, reruns, and performance metrics.
- **Classifier Comparisons**:
  - Compares pairs of classifiers to analyze which one performs better relative to the base truth (`original correctness`).
- **Output Generation**:
  - Saves detailed comparison results, including rows, counts, and average consistency, in a structured JSON file.

## Usage
```bash
python qualitative_analysis_naive_no_fsl.py <path_to_csv>
```

# Script: `postprocessing_new.py`

## Purpose
Processes the raw CSV results of experiments to:
1. Calculate various performance metrics for each classifier (e.g., MCC, F1, accuracy).
2. Analyze agreement and disagreement between classifiers and the baseline (`original correctness`).
3. Generate a detailed report in JSON format to help identify the best-performing classifier.

## Features
- **Preprocessing**:
  - Normalizes correctness values to boolean for consistency.
- **Metrics Calculation**:
  - Calculates MCC, accuracy, precision, recall, F1 score, and balanced accuracy.
- **Agreement Analysis**:
  - Compares classifiers against the baseline (`original correctness`) to compute agreement percentages and confusion matrices.
- **Naive Correctness Analysis**:
  - Identifies cases where `naive correctness` differs or matches other classifiers, with detailed counts and percentages.

## Usage
```bash
python postprocessing_new.py <path_to_csv> <output_json_file>

```

# Script: `not_consistent.py`

## Purpose
Filters and processes consistency results to create progressively filtered versions of the original results. Removes rows with high consistency scores (e.g., `1.0`, `0.9`, etc.) to focus on less consistent or ambiguous cases for further analysis.

## Features
- **Data Augmentation**:
  - Merges consistency scores (from a JSON file) into the results CSV.
  - Adds a `unique_id` column to facilitate consistency mapping.
- **Progressive Filtering**:
  - Creates filtered datasets by removing rows with specific consistency values (`1.0`, `0.9`, `0.8`, etc.).
- **Outputs**:
  - Saves an augmented CSV with consistency scores included.
  - Generates filtered CSVs for different thresholds.

## Usage
```bash
python not_consistent.py <path_to_consistency_json> <path_to_csv>
```

# Script: `not_consistent_naive.py`

## Purpose
Processes consistency results for the naive method to create progressively filtered versions of the original results. Focuses on filtering rows with specific naive consistency scores for further analysis.

## Features
- **Data Augmentation**:
  - Merges naive consistency scores (from a JSON file) into the results CSV.
  - Adds a `unique_id` column to map naive consistencies to results.
- **Progressive Filtering**:
  - Creates filtered datasets by removing rows based on naive consistency thresholds.
- **Outputs**:
  - Saves an augmented CSV with naive consistency scores included.
  - Generates filtered CSVs for different thresholds.

## Usage
```bash
python not_consistent_naive.py <path_to_naive_consistency_json> <path_to_csv>
```


# Script: `not_consistent_naive_no_fsl.py`

## Purpose
Processes consistency results for the naive_no_fsl method to create progressively filtered versions of the original results. Focuses on filtering rows with specific naive_no_fsl consistency scores for further analysis.

## Features
- **Data Augmentation**:
  - Merges naive_no_fsl consistency scores (from a JSON file) into the results CSV.
  - Adds a `unique_id` column to map naive_no_fsl consistencies to results.
- **Progressive Filtering**:
  - Creates filtered datasets by removing rows based on naive_no_fsl consistency thresholds.
- **Outputs**:
  - Saves an augmented CSV with naive_no_fsl consistency scores included.
  - Generates filtered CSVs for different thresholds.

## Usage
```bash
python not_consistent_naive_no_fsl.py <path_to_naive_no_fsl_consistency_json> <path_to_csv>
```

