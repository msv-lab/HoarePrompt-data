def func_1(puzzle1, puzzle2):
    for i in range(4):
        if puzzle1[i] == 'X':
            x1 = i
        if puzzle2[i] == 'X':
            x2 = i
    (puzzle1[x1], puzzle2[x2]) = (puzzle2[x2], puzzle1[x1])
    return sorted(puzzle1) == sorted(puzzle2)
puzzle1 = [input() + input()]
puzzle2 = [input() + input()]
puzzle1 = ''.join(puzzle1).replace('\n', '')
puzzle2 = ''.join(puzzle2).replace('\n', '')
if func_1(puzzle1, puzzle2):
    print('YES')
else:
    print('NO')