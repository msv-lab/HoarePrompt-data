#State of the program right berfore the function call: The input consists of two space-separated integers n and m on the first line, where 1 ≤ n, m ≤ 100. Following n lines contain m characters each, which can be 'R', 'G', or 'B'.
def func():
    n, m = map(int, input().split())

field = [input() for _ in range(n)]

rows = len(set(''.join(field[i::n // 3]) for i in range(n // 3)))

cols = len(set(''.join(row[i * m // 3:(i + 1) * m // 3] for row in field)) for
    i in range(3))

print('YES' if rows == 3 and cols == 3 else 'NO')
#Overall this is what the function does:The function reads two space-separated integers `n` and `m` (where \(1 \leq n, m \leq 100\)) followed by `n` lines of `m` characters each, which can be 'R', 'G', or 'B'. It then processes these inputs to check if the grid can be divided into 3x3 sub-grids such that each sub-grid contains exactly one 'R', one 'G', and one 'B'. If such a division is possible, the function prints 'YES'; otherwise, it prints 'NO'. The function does not handle cases where `n` or `m` are not divisible by 3.

