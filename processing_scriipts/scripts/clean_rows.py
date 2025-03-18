import pandas as pd
import os
import sys



# List of columns to validate
# TESTED_COLUMNS = ["original correctness", "summary fsl", "naive correctness fsl", "vanilla", "simple tree", "complex tree",  "summary" , "simple verify fsl", "complex verify fsl", "summary verify fsl", "simple verify", "complex verify", "summary verify"]
TESTED_COLUMNS = ["original correctness",  "vanilla",  "complex tree"]
def clean_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Standardize the tested columns to have boolean values
    def clean_value(value):
        if pd.isna(value):
            return None
        str_val = str(value).strip().lower()
        if str_val in ["true", "t", "1"]:
            return True
        elif str_val in ["false", "f", "0"]:
            return False
        return None

    # Apply cleaning to tested columns
    for col in TESTED_COLUMNS:
        if col in df.columns:
            df[col] = df[col].apply(clean_value)
        else:
            print(f"Warning: Column '{col}' not found in the CSV.")

    # Count initial number of rows
    initial_row_count = len(df)

    # Filter out rows with any invalid values in the tested columns
    df_cleaned = df.dropna(subset=TESTED_COLUMNS, how='any')

    # Count final number of rows
    final_row_count = len(df_cleaned)

    # Calculate number of rows removed
    rows_removed = initial_row_count - final_row_count

    # Save the cleaned CSV with a new name
    base_name, ext = os.path.splitext(file_path)
    cleaned_file_path = f"{base_name}_cleaned{ext}"
    df_cleaned.to_csv(cleaned_file_path, index=False)

    print(f"Cleaned file saved as: {cleaned_file_path}")
    print(f"Rows removed: {rows_removed}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <input_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]

    if not os.path.isfile(input_csv):
        print(f"Error: The file '{input_csv}' does not exist.")
        sys.exit(1)

    clean_csv(input_csv)
