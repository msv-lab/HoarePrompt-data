(n, m, k, x, y) = map(int, input().split())
x -= 1
y -= 1
full_cycle_length = (2 * n - 2) * m if n > 1 else m
full_cycles = k // full_cycle_length
remaining_questions = k % full_cycle_length
min_questions = full_cycles
max_questions = full_cycles
if n > 1:
    min_questions = full_cycles // (2 * n - 2)
    max_questions = (full_cycles + n - 1) // (2 * n - 2)
sergei_questions = min_questions
if x == 0 or x == n - 1:
    sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1)
else:
    sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 * n - 2) >= x)
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