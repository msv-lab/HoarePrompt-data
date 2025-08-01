import io
import sys
from program import *

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

# Test case 1
input_data = """5 5
.. R1 .. B1 ..
RG .. .. .. BG
RG R0 .Q B0 BG
RG .. .. .. BG
.. R2 .. B2 ..
13
B2 U
B2 U
B2 L
B2 C .Q
B2 L
B2 L
B2 T
R0 R
R0 C .Q
R0 D
R0 R
R0 R
R0 T"""
expected_output = """6 BLUE GOAL
12 RED GOAL
FINAL SCORE: 1 1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2
input_data = """3 5
.. .. R0 .. ..
RG .. .Q .. BG
.. .. B0 .. ..
12
R0 D
R0 C .Q
R0 R
R0 T
R0 D
B0 R
B0 U
B0 C .Q
B0 L
B0 L
B0 L
B0 T"""
expected_output = """11 BLUE GOAL
FINAL SCORE: 0 1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3
input_data = """3 5
.. .. R0 .. ..
RG .. .Q .. BG
.. .. B0 .. ..
5
R0 D
R0 C .Q
R0 L
R0 L
R0 T"""
expected_output = """4 BLUE GOAL
FINAL SCORE: 0 1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: No goals scored
input_data = """3 5
.. .. R0 .. ..
RG .. .Q .. BG
.. .. B0 .. ..
0"""
expected_output = """FINAL SCORE: 0 0"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Multiple goals by one team
input_data = """5 5
.. R1 .. B1 ..
RG .. .. .. BG
RG R0 .Q B0 BG
RG .. .. .. BG
.. R2 .. B2 ..
18
B2 U
B2 U
B2 L
B2 C .Q
B2 L
B2 L
B2 T
R0 R
R0 C .Q
R0 D
R0 R
R0 R
R0 T
B2 U
B2 U
B2 L
B2 C .Q
B2 L
B2 L
B2 L
B2 T"""
expected_output = """6 BLUE GOAL
12 RED GOAL
18 BLUE GOAL
FINAL SCORE: 1 2"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Edge case with minimal field size and players
input_data = """3 3
RG .. BG
.. .Q ..
R0 .. B0
4
R0 R
R0 C .Q
R0 R
R0 T"""
expected_output = """3 BLUE GOAL
FINAL SCORE: 0 1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7: Quaffle thrown without being caught
input_data = """3 3
RG .. BG
.. .Q ..
R0 .. B0
2
R0 R
R0 T"""
expected_output = """FINAL SCORE: 0 0"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 8: Players moving around without scoring
input_data = """3 3
RG .. BG
.. .Q ..
R0 .. B0
8
R0 R
R0 U
R0 L
R0 D
B0 R
B0 U
B0 L
B0 D"""
expected_output = """FINAL SCORE: 0 0"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 9: Players scoring in their own goal
input_data = """3 3
RG .. BG
.. .Q ..
R0 .. B0
6
R0 R
R0 C .Q
R0 R
R0 R
R0 T
B0 L
B0 C .Q
B0 L
B0 L
B0 T"""
expected_output = """4 BLUE GOAL
10 RED GOAL
FINAL SCORE: 1 1"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 10: Multiple goals and multiple players
input_data = """5 5
RG .. BG .. ..
.. R0 .. B0 ..
.. .Q .. .. ..
.. R1 .. B1 ..
RG .. BG .. ..
12
R0 R
R0 C .Q
R0 R
R0 T
B0 L
B0 C .Q
B0 L
B0 T
R1 R
R1 C .Q
R1 R
R1 T"""
expected_output = """3 BLUE GOAL
7 RED GOAL
11 BLUE GOAL
FINAL SCORE: 1 2"""
assert run_program_with_captured_io(input_data) == expected_output

# End of script