import json
from pathlib import Path
from datetime import datetime
from model import get_model
import re

ORDER_ANALYSIS_PROMPT = """
You are an expert in competitive programming and algorithms. Your task is to analyze whether the order of elements in the output matters for a given programming problem.

Here is the problem description:

{question}

Please analyze whether the order of elements in the output matters. Answer with just "YES" if the order matters, or "NO" if the order doesn't matter.

For example:
- If the problem asks to sort numbers in ascending order, the order matters (YES)
- If the problem asks to find any valid solution where elements can be in any order, the order doesn't matter (NO)
- If the problem asks to output the minimum number of operations, the order doesn't matter (NO)
- If the problem asks to output a specific sequence of operations that must be performed in order, the order matters (YES)

Answer with just YES or NO:
"""

CASE_SENSITIVITY_PROMPT = """
You are an expert in competitive programming and algorithms. Your task is to analyze whether the case (uppercase or lowercase) of characters in the output matters for a given programming problem.

Here is the problem description:

{question}

Please analyze whether the case of characters in the output matters. Answer with just "YES" if case sensitivity matters, or "NO" if case sensitivity doesn't matter.

For example:
- If the problem specifies that uppercase and lowercase are treated differently, case sensitivity matters (YES).
- If the problem allows the output to be in any case, case sensitivity doesn't matter (NO).
- If the problem is about finding strings or patterns with exact case, case sensitivity matters (YES).

Answer with just YES or NO:
"""

def remove_assert_statements(code_str):
    assert_pattern = r'^\s*assert.*(?:\r\n|\n|\r)?'
    cleaned_code = re.sub(assert_pattern, '', code_str, flags=re.MULTILINE)
    return cleaned_code

def analyze_order_sensitivity(prompt, model):
    ans = False
    prompt = ORDER_ANALYSIS_PROMPT.format(question=prompt)
    prompt = remove_assert_statements(prompt)
    response = model.query(prompt)
    response = response.strip().upper()
    ans = (response != "YES")
    return ans


def analyze_case_sensitivity(prompt, model):
    """
    Analyzes whether case sensitivity matters in the given problem description.

    Args:
        prompt (str): The programming problem description.
        model: The language model instance to query.

    Returns:
        bool: True if case sensitivity doesn't matter, False if it matters.
    """
    prompt = CASE_SENSITIVITY_PROMPT.format(question=prompt)
    prompt = remove_assert_statements(prompt)  # Reuse the function to clean the prompt.
    response = model.query(prompt)
    response = response.strip().upper()
    is_insensitive = (response != "YES")  # Case doesn't matter if response is NOT "YES".
    return is_insensitive