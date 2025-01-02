sys.setrecursionlimit(2 ** 15)
board = []
painted_rows = [False] * 8
painted_cols = [False] * 8

def func_1(col_num):
    painted_by_rows = True
    for (row_num, x) in enumerate(board):
        if x[col_num] != True:
            return False
        painted_by_rows = painted_by_rows and painted_rows[row_num]
    return True and (not painted_by_rows)

def func_2():
    for y in xrange(8):
        board.append([True if x == 'B' else False for x in raw_input()])
    strokes = 0
    for (row_num, row) in enumerate(board):
        if all(row):
            strokes += 1
            painted_rows[row_num] = True
    for col_num in xrange(8):
        if func_1(col_num):
            strokes += 1
            painted_cols[col_num] = True
    print(strokes)
func_2()