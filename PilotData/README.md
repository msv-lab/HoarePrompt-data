# Pilot Data Generation

This project generates code using specified Large Language Models (LLMs) for tasks from the APPS benchmark and MBPP plus benchmark, and evaluates the correctness of the generated code.

## Usage

- To generate a set of APPS benchmark data, run the following command:
  ```bash
  python3 apps_code_gen.py
  ```
- To generate a set of MBPP plus benchmark data, run the following command:
  ```bash
  python3 mbpp_code_gen.py
  ```

**Note**: Ensure the correct location for `APPS` directory is set before running, as the required files for APPS are not included in the repository due to their large size.

## Few-shot example

- `apps_code_gen.py` uses `0000` and `2747` as few-shot examples for the APPS benchmark.
- `mbpp_code_gen.py` uses examples from `Mbpp/2`, `Mbpp/3`, and `Mbpp/4` for few-shot examples in the MBPP plus benchmark.

## Testing

- The testing strategy follows a method similar to the original authors.
  - For MBPP, the correct output is obtained by running the `canonical_solution` using Python's `exec()` with the provided inputs.
  - For APPS, the output is captured using `subprocess` to handle the standard output.

**Note**: MBPP task `255` is skipped due to the potential complexity in the LLM-generated answers.

## Random Selection

To perform random selection of data, use the following command:
```bash
python3 random_select.py
```
