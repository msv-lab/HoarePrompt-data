#!/bin/bash

# Usage: ./run_analysis.sh confidence_naive.json confidence_naive_no_fsl.json original_results.csv

# Check if correct arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <confidence_naive.json> <confidence_naive_no_fsl.json> <original_results.csv>"
    exit 1
fi

# Arguments
CONFIDENCE_NAIVE_JSON=$1
CONFIDENCE_NAIVE_NO_FSL_JSON=$2
ORIGINAL_RESULTS_CSV=$3

# Run initial Python scripts
python3 not_consistent_naive.py "$CONFIDENCE_NAIVE_JSON" "$ORIGINAL_RESULTS_CSV"
python3 not_consistent_naive_no_fsl.py "$CONFIDENCE_NAIVE_NO_FSL_JSON" "$ORIGINAL_RESULTS_CSV"

# Define base directory where files are created
BASE_DIR=$(dirname "$ORIGINAL_RESULTS_CSV")

AUGMENTED_NAIVE="augmented_naive.csv"
AUGMENTED_NAIVE_NO_FSL="augmented_naive_no_fsl.csv"

FILTERED_FILES=(
    "filtered_consistency_1_56_46_naive_no_fsl.csv"
    "filtered_consistency_1_56_46_naive.csv"
    "filtered_consistency_1_56_naive_no_fsl.csv"
    "filtered_consistency_1_56_naive.csv"
    "filtered_consistency_1_naive_no_fsl.csv"
    "filtered_consistency_1.csv"
)

# Run postprocessing for each file
echo "Running postprocessing for generated files..."


for FILE in "${AUGMENTED_NAIVE}" "${AUGMENTED_NAIVE_NO_FSL}" "${FILTERED_FILES[@]}"; do
    FILE_PATH="${BASE_DIR}/${FILE}"

    FILE_NAME=$(basename "${FILE}" .csv)
    if [ -f "${FILE_PATH}" ]; then
        python3 postprocessing_new.py "${FILE_PATH}" "${BASE_DIR}/${FILE_NAME}_results.json"
        echo "Processed: ${FILE_PATH}"
    else
        echo "Warning: File not found: ${FILE_PATH}"
    fi
done

# Run consistency correlation scripts
echo "Running consistency correlation..."
python3 consistency_correlation_naive.py "${BASE_DIR}/${AUGMENTED_NAIVE}" 
python3 consistency_correlation_naive_no_fsl.py "${BASE_DIR}/${AUGMENTED_NAIVE_NO_FSL}" 

# Run qualitative analysis scripts
echo "Running qualitative analysis..."
python3 qualitative_analysis_naive.py "${BASE_DIR}/${AUGMENTED_NAIVE}" 
python3 qualitative_analysis_naive_no_fsl.py "${BASE_DIR}/${AUGMENTED_NAIVE_NO_FSL}"

echo "All tasks completed successfully."
