# HoarePrompt Experiment Results

## Overview

This folder contains the results of our experiments with the HoarePrompt tool across multiple datasets and classifiers. The structure is divided into **four main subfolders**:

1. **Dataset** – Contains the full dataset used in our experiments.
2. **Qwen7** – Results from the Qwen2.5-7B-instruct model.
3. **Qwen32** – Results from the Qwen2.5-32B-instruct model.
4. **Qwen72** – Results from the Qwen2.5-72B-instruct model.

Each model-specific folder follows an identical internal structure, as described below.

The averages.json file contains the averagesmetrics for the 5 classifiers acroiss the 3 models.
---

## Dataset Folder

The **Dataset** folder contains:

- **`CoCoClaNel_with_pilot.json`** – The complete dataset with **785 problem-code pairs**.
- **`CoCoClaNel_pilot.json`** – The **pilot dataset** used for tool calibration and debugging (**140 problems**).
- **`CoCoClaNel_experiments.json`** – The **remaining 645 problems** used for actual experiments.
- **Six split files (`code_force_2024_final_random1` to `code_force_2024_final_random6`)** – Randomly split subsets of the experiment dataset to facilitate pipelining.

---

## Model-Specific Folders (Qwen7, Qwen32, Qwen72)

Each model folder (`Qwen7`, `Qwen32`, `Qwen72`) contains results from experiments conducted with that model. These folders have an identical structure:

- **`normal/`** – Contains results from the **Vanilla, Zero-Shot-CoT, and HoarePrompt classifiers**.
- **`unroll/`** – Contains results from the **HoarePrompt No-Unroll classifier**.
- **`tester/`** – Contains results from the **Tester classifier**.
- **`results.json`** – A JSON file summarizing the **metrics of all classifiers** used with this model.

### Inside a Model's `normal/` Folder

For example, inside `Qwen72/normal/`, you will find:

- **`tokens.json`** – Tracks token usage with Few-Shot Learning (FSL) examples.
- **`tokens_no_fsl.json`** – Tracks token usage without FSL examples.
- **`results.json`** – Summary metrics of the classifiers.
- **`total.csv`** – A CSV file containing all results in tabular format.
- **Subfolders for each dataset split** (e.g., `code_force_2024_final_random1`, `code_force_2024_final_random2`, etc.)

### Inside Each Dataset Split Folder

Each dataset split folder (e.g., `Qwen72/normal/code_force_2024_final_random1/`) contains **three subfolders**, each corresponding to a different rerun of the experiment for result stability.

Within these rerun subfolders, you will find directories for **each unique problem-code combination**, containing:

- **`description.txt`** – The problem description.
- **`program.py`** – The program code.
- **`extract-precondition/`** – The computed precondition.
- **`compute-postcondition/`** – The computed postcondition.
- **`check-entailment/`** – Final entailment calls for each classifier when correctness is determined.

### Classifier-Specific Entailment Files

In `check-entailment/`, the final model decisions are recorded:

- **`entailment-complex/`** – Corresponds to **HoarePrompt**.
- **`entailment_vanilla/`** – Corresponds to **Zero-Shot-CoT**.
- **`entailment_vanilla_no_cot/`** – Corresponds to **Vanilla (no CoT)**.

For **Tester classifier experiments**, the structure is simpler. Instead of multiple subfolders, there is just **one prompt and one response** stored in the main directory.

---

## Postprocessing the Results

### Converting CSV Results to JSON Metrics

You can convert CSV result files into JSON-format metrics using the following scripts located in the **`../scripts/`** directory:

- **For Vanilla, Zero-Shot-CoT, and HoarePrompt classifiers:**
  ```bash
  python3 ../scripts/postprocessing.py  /path/to/results.csv  /path/to/output.json
  ```

- **For HoarePrompt No-Unroll classifier:**
  ```bash
  python3 ../scripts/postprocessing_unroll.py  /path/to/results.csv  /path/to/output.json
  ```

- **For Tester classifier:**
  ```bash
  python3 ../scripts/postprocessing_tester.py  /path/to/results.csv  /path/to/output.json
  ```

These scripts extract metrics from the CSV files and format them into structured JSON summaries.

---

