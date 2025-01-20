#State of the program right berfore the function call: The input consists of two space-separated integers n and m representing the dimensions of the field (1 ≤ n, m ≤ 100), followed by n lines, each containing m characters that are either 'R', 'G', or 'B'.
def func():
    n, m = map(int, input().split())

field = [input() for _ in range(n)]

rows = len(set(''.join(field[i::n // 3]) for i in range(n // 3)))

cols = len(set(''.join(row[i * m // 3:(i + 1) * m // 3] for row in field)) for
    i in range(3))

print('YES' if rows == 3 and cols == 3 else 'NO')
#Overall this is what the function does:The function processes a matrix of dimensions `n` by `m` where each element is either 'R', 'G', or 'B'. It checks whether the matrix can be divided into 3x3 submatrices such that each submatrix contains exactly one 'R', one 'G', and one 'B'. If all such 3x3 submatrices meet this condition, the function returns 'YES'; otherwise, it returns 'NO'.

