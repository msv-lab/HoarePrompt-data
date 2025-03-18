import io
import sys

def run_program_with_captured_io(input_data):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        with open("program.py", "r", encoding="utf-8") as f:
            code = f.read()
            exec(code, {})

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Test cases
test_cases = [
    ("5\n24\n70\n3\n55\n48", "aav\nrzz\naaa\nczz\nauz"),
    ("1\n78", "zzz"),
    ("1\n3", "aaa"),
    ("1\n52", "azy"),
    ("1\n53", "bzz"),
    ("1\n54", "caz"),
    ("1\n55", "czz"),
    ("1\n56", "daz"),
    ("1\n57", "dbz"),
    ("1\n58", "dcz"),
    ("1\n59", "ddz"),
    ("1\n60", "dez"),
    ("1\n61", "dfz"),
    ("1\n62", "dgz"),
    ("1\n63", "dhz"),
    ("1\n64", "diz"),
    ("1\n65", "dzd"),
    ("1\n66", "dze"),
    ("1\n67", "dzf"),
    ("1\n68", "dzg"),
    ("1\n69", "dzh"),
    ("1\n70", "dzi"),
    ("1\n71", "dzj"),
    ("1\n72", "dzk"),
    ("1\n73", "dzl"),
    ("1\n74", "dzm"),
    ("1\n75", "dzn"),
    ("1\n76", "dzo"),
    ("1\n77", "dzp"),
    ("1\n78", "dzq"),
]

# Run tests
for i, (input_data, expected_output) in enumerate(test_cases):
    assert run_program_with_captured_io(input_data) == expected_output, f"Test case {i+1} failed"

print("All test cases passed!")