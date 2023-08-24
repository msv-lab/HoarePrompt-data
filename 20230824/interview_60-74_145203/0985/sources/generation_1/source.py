def count_attacking_pairs(n, bishops):
    pair_count = 0
    row_diagonal_count = [0] * 2001
    col_diagonal_count = [0] * 2001

    for bishop in bishops:
        row, col = bishop
        diagonal = row + col
        reverse_diagonal = row - col + 1000

        pair_count += row_diagonal_count[diagonal]
        pair_count += col_diagonal_count[reverse_diagonal]

        row_diagonal_count[diagonal] += 1
        col_diagonal_count[reverse_diagonal] += 1

    return pair_count


n = int(input())
bishops = [list(map(int, input().split())) for _ in range(n)]

result = count_attacking_pairs(n, bishops)
print(result)