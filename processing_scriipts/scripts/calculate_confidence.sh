#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_csv>"
    exit 1
fi

# Input CSV file
INPUT_CSV="$1"

# Check if the input file exists
if [ ! -f "$INPUT_CSV" ]; then
    echo "Error: File '$INPUT_CSV' does not exist."
    exit 1
fi

# Run the Python script
python3 calculate_confidence_simple.py "$INPUT_CSV"
python3 calculate_confidence_naive.py "$INPUT_CSV"
python3 calculate_confidence_naive_no_fsl.py "$INPUT_CSV"