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

# Script: `majority_csv.py`

## Purpose
Processes multiple CSV files to compute the majority vote for specific columns grouped by `Task ID` and `model_created`. The resulting CSV contains the most common classification for each code example, summarizing classifier results.

## Features
- **CSV Consolidation**:
  - Finds and processes all CSV files in a specified directory (including subdirectories). You can specify that directory by adding the path in the script.
  - Combines them into a single dataset.
- **Majority Vote**:
  - Groups rows by `Task ID` and `model_created`.
  - Computes the most common value (majority vote) for key columns.
- **Output**:
  - Generates a new CSV with the majority vote for each group.

## Usage
```bash
python majority_csv.py
```
# Script: `functions_num_correlation.py`

## Purpose
Analyzes the correlation between:
1. **Number of functions** in a program example.
2. **Presence of multiple functions** in an example.
And the **success of various classifiers**. The goal is to determine if the number of functions impacts classifier performance.

## Features
- **Metrics Calculation**:
  - Compares each classifier's correctness relative to `naive no fsl` using the original correctness as the ground truth.
  - Assigns scores based on whether the classifier or `naive no fsl` outperformed the other.
- **Correlation Analysis**:
  - Calculates the correlation between:
    - Classifier performance and the number of functions (`functions` column).
    - Classifier performance and a boolean indicating single or multiple functions (`functions_small` column: True for ≤ 1 function, False otherwise).
- **Output Results**:
  - Saves correlation results as a CSV file for further analysis.

## Usage
```bash
python functions_num_correlation.py <path_to_csv>
```

# Script: `find_uncalled_functions.py`

## Purpose
Identifies examples in a dataset where functions are defined but never invoked. This helps detect potential issues in generated or manually written code, such as incomplete or redundant functions.

## Features
- **Function Detection**:
  - Parses Python scripts to extract all defined functions.
  - Identifies functions that are defined but never called within the same script.
- **JSON Processing**:
  - Analyzes a dataset JSON file to find examples with uninvoked functions.
  - Outputs a list of task IDs and models where such cases occur.

## Usage
```bash
python find_uncalled_functions.py <path_to_json_file>
```

# Script: `find_max_loop_depth.py`

## Purpose
Analyzes a dataset of Python programs to determine the maximum loop depth (nested loops) in each example. Filters the dataset to retain only examples with a loop depth of 1 or 2, removing outliers.

## Features
- **Loop Depth Calculation**:
  - Traverses the abstract syntax tree (AST) of each program to compute the maximum nesting level of loops (`for`, `while`).
- **Error Handling**:
  - Assigns a depth of `-1` to programs that cannot be parsed.
- **Filtering**:
  - Retains only examples with a loop depth of `1` or `2`.


### Input
- **Dataset JSON**:
  - Each entry should include:
    - `generated_code`: The Python code to analyze.

### Output
- **Cleaned Dataset JSON**:
  - Includes only entries with valid loop depths (`1` or `2`).
  - Adds a new field `depth` to each entry indicating the maximum loop depth.


## Usage
Change the hardcoded paths to your desired ones
```bash
python find_max_loop_depth.py  
```

# Script: `consistency_correlation.py`, `consistency_correlation_naive.py`, `consistency_correlation_naive_no_fsl.py`

## Purpose
Analyzes the correlation between consistency metrics (calculated from a JSON file) and the performance of various classifiers. Helps identify which classifiers perform better or worse for examples with high or low consistency.

Use `consistency_correlation_naive.py` for consistencies of the naive approcah.
Use `consistency_correlation_naive_no_fsl.py` for consistencies of the naive_no_fsl approcah.

## Features
- **Consistency Correlation**:
  - Computes the Pearson correlation between consistency and classifier performance.
- **Classifier Comparison**:
  - Compares `naive no FSL correctness` against other classifiers to determine performance trends.
- **Metrics Calculation**:
  - Uses metrics like accuracy, precision, recall, and F1-score to assess correlations.
- **Correlation Output**:
  - Saves the correlation results for each classifier to a CSV file.

## Input
- **CSV File**:
  - Contains the results of classifiers for various examples.
  - Required columns: 
    - `Correctness`, `naive correctness`, `original correctness`, 
    - `annotated correctness`, `annotated correctness simple`, 
    - `naive no fsl correctness`, `Correctness no fsl`.
  - Consistency values are also included for each example.

## Output
- **CSV File**:
  - Saves correlation results in a new file named `consistency_analysis_results.csv`.

### Key Outputs
- **Positive Correlation**:
  - High consistency is associated with better performance of the classifier relative to others.
- **Negative Correlation**:
  - High consistency is associated with worse performance of the classifier relative to others.
- **Zero Correlation**:
  - Indicates no strong relationship between consistency and classifier performance.


## Usage
Change the hardcoded paths to your desired ones
```bash
python consistency_correlation.py <path_to_csv>
```

# Script: `concat_csv.py`

## Purpose
Concatenates all CSV files from the immediate subdirectories of a given directory into a single combined CSV file.

## Features
- **CSV File Aggregation**:
  - Automatically traverses one level of subdirectories in the specified input directory.
  - Collects all `.csv` files within these subdirectories.
- **Dataframe Concatenation**:
  - Combines the collected CSV files into a single unified DataFrame.
- **Output Generation**:
  - Saves the combined DataFrame to a specified output CSV file.

## Input
- **Directory**:
  - The directory containing subdirectories with CSV files to concatenate.
- **CSV Files**:
  - All `.csv` files within the first level of subdirectories will be processed.

## Output
- **Combined CSV File**:
  - A single file that merges all input CSV files.

## Usage
```bash
python concat_csv.py <input_directory> <output_csv>
```



# Script: `concat_csv_temp.py`

## Purpose
Concatenates specific CSV files into a single combined CSV file. The paths to the input files and the output file are hardcoded and can be modified as needed.

## Features
- **CSV File Aggregation**:
  - Combines pre-defined CSV files into a single unified DataFrame.
- **Customizable Paths**:
  - Input and output file paths can be adjusted to meet specific requirements.
- **Output Generation**:
  - Saves the concatenated DataFrame to a specified output file.

## Input
- **Hardcoded CSV Paths**:
  - Example paths are pre-specified in the script. These should be updated based on the files you wish to combine.

## Output
- **Combined CSV File**:
  - A single file containing all rows from the input CSV files.

## Usage
The script does not accept command-line arguments. Update the hardcoded paths directly in the script to include desired files.


# Script: `clean_rows.py`

## Purpose
Cleans a CSV file by validating specific classifier result columns to ensure that all values are boolean (`True` or `False`). Rows with invalid or missing values in these columns are removed.

## Features
- **Validation of Classifier Columns**:
  - Ensures specified columns only contain valid boolean values (`True`, `False`, `t`, `f`, `1`, `0`).
- **Row Filtering**:
  - Removes rows with invalid or missing values in the tested columns.
- **Output**:
  - Saves a cleaned version of the CSV file with invalid rows removed.

## Input
- **CSV File**:
  - Path to the input CSV file containing classifier results.
- **Tested Columns**:
  - The script validates the following columns (if present in the CSV):
    - `Correctness`
    - `original correctness`
    - `naive correctness`
    - `annotated correctness`
    - `annotated correctness simple`
    - `naive no fsl correctness`
    - `Correctness no fsl`
    - `simple verify`
    - `complex verify`
    - `default verify`
    - `simple verify no fsl`
    - `complex verify no fsl`
    - `default verify no fsl`

## Output
- **Cleaned CSV File**:
  - A new CSV file with "_cleaned" appended to the original file name.
  - Rows containing invalid or missing values in the tested columns are removed.
- **Summary**:
  - The number of rows removed is printed to the console.

## Usage
Run the script from the command line:
```bash
python clean_rows.py <input_csv>
```

# Script: `calculate_confidence_simple.py`

## Purpose
Calculates the confidence of classifier results for code examples based on repeated run results stored in a CSV. The confidence is derived as the average consistency of the "naive" and "naive no FSL" classifiers.

## Features
- **Consistency Metrics**:
  - Computes the consistency of classifiers (`naive correctness` and `naive no fsl correctness`) by analyzing their repeated predictions.
- **Group-Level Consistency**:
  - Groups results by `unique_id` and calculates per-group consistency for both classifiers.
  - Aggregates overall consistency across all groups.
- **Correct and Incorrect Responses**:
  - Separately calculates consistency metrics for majority-correct and majority-incorrect responses.
- **Summary Statistics**:
  - Provides average and median consistency metrics for:
    - All examples
    - Majority-correct examples
    - Majority-incorrect examples

## Input
- **CSV File**:
  - Path to the input CSV file containing classifier predictions and the ground truth.

## Output
- **JSON File**:
  - Outputs a JSON file named `confidence.json` in the same directory as the input CSV.
  - The JSON includes:
    - Group-wise consistency for each `unique_id`.
    - Summary statistics on consistency.

## Usage
Run the script from the command line:
```bash
python calculate_confidence_simple.py <input_csv>
```

# Script: `calculate_confidence_naive.py`

## Purpose
Calculates the confidence of classifier results for code examples based on repeated "naive" classifier runs stored in a CSV. The confidence is derived solely from the "naive correctness" responses.

## Features
- **Consistency Metrics**:
  - Computes the consistency of the "naive correctness" classifier by analyzing repeated predictions.
- **Group-Level Consistency**:
  - Groups results by `unique_id` and calculates per-group consistency for the "naive correctness" classifier.
- **Summary Statistics**:
  - Provides average and median consistency metrics for:
    - All examples
    - Majority-correct examples
    - Majority-incorrect examples

## Input
- **CSV File**:
  - Path to the input CSV file containing classifier predictions and the ground truth.

## Output
- **JSON File**:
  - Outputs a JSON file named `confidence_naive.json` in the same directory as the input CSV.
  - The JSON includes:
    - Group-wise consistency for each `unique_id`.
    - Summary statistics on consistency.

## Usage
Run the script from the command line:
```bash
python calculate_confidence_naive.py <input_csv>
```

# Script: `calculate_confidence_naive_no_fsl.py`

## Purpose
Calculates the confidence of classifier results for code examples based on repeated "naive no FSL" classifier runs stored in a CSV. The confidence is derived solely from the "naive no fsl correctness" responses.

## Features
- **Consistency Metrics**:
  - Computes the consistency of the "naive no fsl correctness" classifier by analyzing repeated predictions.
- **Group-Level Consistency**:
  - Groups results by `unique_id` and calculates per-group consistency for the "naive no fsl correctness" classifier.
- **Summary Statistics**:
  - Provides average and median consistency metrics for:
    - All examples
    - Majority-correct examples
    - Majority-incorrect examples

## Input
- **CSV File**:
  - Path to the input CSV file containing classifier predictions and the ground truth.

## Output
- **JSON File**:
  - Outputs a JSON file named `confidence_naive_no_fsl.json` in the same directory as the input CSV.
  - The JSON includes:
    - Group-wise consistency for each `unique_id`.
    - Summary statistics on consistency.

## Usage
Run the script from the command line:
```bash
python calculate_confidence_naive_no_fsl.py <input_csv>
```

# Script: `calculate_confidence_logprobs.py`

## Purpose
Calculates the confidence of classifier results for code examples using token probabilities (`logprobs`) stored in a CSV. Confidence is determined by summing the probabilities for the majority responses and subtracting probabilities for non-majority responses.

## Features
- **Weighted Confidence**:
  - Uses token probabilities (`logprobs`) to calculate a weighted consistency score.
- **Majority Response Contribution**:
  - Adds the probabilities for majority responses and subtracts those for non-majority responses.
- **Group-Level Consistency**:
  - Groups results by `unique_id` and calculates consistency metrics.
- **Summary Statistics**:
  - Provides average and median consistency metrics for:
    - All examples
    - Majority-correct examples
    - Majority-incorrect examples

## Input
- **CSV File**:
  - Path to the input CSV file containing `naive no fsl correctness`, `original correctness`, and `logprobs`.

## Output
- **JSON File**:
  - Outputs a JSON file named `confidence_new_metric.json` in the same directory as the input CSV.
  - The JSON includes:
    - Group-wise consistency for each `unique_id`.
    - Summary statistics on consistency (new weighted metric and old unweighted metric).

## Usage
Run the script from the command line:
```bash
python calculate_confidence_logprobs.py <input_csv>
```

# Script: `aggregate_json.py`

## Purpose
Aggregates the results of multiple analysis JSON files by combining them and calculating averages for numerical fields. Useful for consolidating results from different runs of a dataset.

## Features
- **Recursive Aggregation**:
  - Combines numerical values across multiple JSON files by summing and averaging.
- **Flexible Input**:
  - Handles nested dictionaries in JSON files, calculating averages for each level.
- **Static Paths**:
  - Paths for input JSON files and output JSON are hardcoded but can be modified directly in the script.

## Input
- **JSON Files**:
  - Paths to input JSON files containing analysis results. thye must be hardcoded

## Output
- **JSON File**:
  - Outputs an aggregated JSON file with averaged values for numerical fields.

## How It Works
1. **Load JSON Data**:
   - Reads multiple JSON files specified in the script.
2. **Aggregate Data**:
   - Sums numerical values and tracks their counts.
   - For non-numerical fields (e.g., strings), retains the first encountered value.
3. **Calculate Averages**:
   - Divides summed values by their counts to compute averages.
4. **Save Results**:
   - Writes the averaged data to a new JSON file.

## Usage
Run the script directly. Modify the file paths for input and output as needed.

### Example
```bash
python aggregate_json.py
```

# Script: `postprocessing.sh`

## Purpose
Automates the postprocessing pipeline for generating analysis metrics from raw CSV results and confidence (consistency) JSON files. It combines several Python scripts to produce comprehensive analysis outputs.

## Features
- **Automated Workflow**:
  - Processes raw results and confidence data to generate augmented datasets and filtered results.
- **Multiple Analyses**:
  - Runs scripts for qualitative analysis, consistency correlation, and other metrics.
- **Flexible Inputs**:
  - Accepts confidence JSON files and a CSV file as inputs.

## Usage
Run the script from the command line with three arguments:
1. **`confidence_naive.json`**: Path to the naive confidence JSON file.
2. **`confidence_naive_no_fsl.json`**: Path to the naive no FSL confidence JSON file.
3. **`original_results.csv`**: Path to the original CSV results file.

### Example
```bash
./postprocessing.sh confidence_naive.json confidence_naive_no_fsl.json original_results.csv
```