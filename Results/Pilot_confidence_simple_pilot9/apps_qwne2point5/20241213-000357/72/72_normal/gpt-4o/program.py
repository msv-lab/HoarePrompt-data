n, m, k, x, y = map(int, input().split())

# Convert 1-based indices to 0-based for easier calculations
x -= 1
y -= 1

# Calculate the number of complete cycles (from 1st row to nth row and back to 1st)
full_cycle_length = (2 * n - 2) * m if n > 1 else m

# Calculate the number of complete cycles that fit into k questions
full_cycles = k // full_cycle_length

# Calculate the remaining questions after the full cycles
remaining_questions = k % full_cycle_length

# Initialize the counts for each pupil
min_questions = full_cycles
max_questions = full_cycles

# Handle special cases for first row and last row
if n > 1:
    min_questions = full_cycles // (2 * n - 2)
    max_questions = (full_cycles + n - 1) // (2 * n - 2)

# Calculate the number of times Sergei is asked
sergei_questions = min_questions
if x == 0 or x == n - 1:  # First or last row
    sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1)
else:
    sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 * n - 2) >= x)

# Process the remaining questions
row = 0
direction = 1
for _ in range(remaining_questions):
    for col in range(m):
        if row == x and col == y:
            sergei_questions += 1
        if direction == 1:
            max_questions += 1
            row += direction
            if row == n:
                direction = -1
                row -= 2
        else:
            max_questions -= 1
            row += direction
            if row == -1:
                direction = 1
                row += 2

print(max_questions, min_questions, sergei_questions)
