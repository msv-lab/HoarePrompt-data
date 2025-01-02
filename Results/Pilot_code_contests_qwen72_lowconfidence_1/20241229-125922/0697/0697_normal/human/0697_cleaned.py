(n, m) = map(int, raw_input().split(' '))
lines = stdin.readlines()
rows = [None] * n
for i in xrange(n):
    rows[i] = map(int, lines[i].split(' '))

def func_1(xs):
    """example: [10,20,14,10] -> ([1,3,2,1], 3). returns list of positive integers with equivalent pairwise comparisons (<,=,>) to list."""
    xs = sorted([xs[i] * 1000 + i for i in xrange(len(xs))])
    ys = [0] * len(xs)
    last_x = None
    j = 0
    for w in xs:
        x = w / 1000
        i = w % 1000
        if x == last_x:
            ys[i] = j
        else:
            j += 1
            ys[i] = j
        last_x = x
    return (ys, j)
columns = [[rows[i][j] for i in xrange(n)] for j in xrange(m)]
rows_ordered = [func_1(row) for row in rows]
columns_ordered = [func_1(column) for column in columns]

def func_2(i, j):
    if rows_ordered[i][0][j] > columns_ordered[j][0][i]:
        difference = rows_ordered[i][0][j] - columns_ordered[j][0][i]
        return max(rows_ordered[i][1], columns_ordered[j][1] + difference)
    else:
        difference = columns_ordered[j][0][i] - rows_ordered[i][0][j]
        return max(columns_ordered[j][1], rows_ordered[i][1] + difference)
answer_matrix = [[func_2(i, j) for i in xrange(n)] for j in xrange(m)]
stdout.write('\n'.join([' '.join([str(answer_matrix[j][i]) for j in xrange(m)]) for i in xrange(n)]))