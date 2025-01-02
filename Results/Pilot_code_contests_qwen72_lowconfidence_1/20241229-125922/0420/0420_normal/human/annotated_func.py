#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 50. The grid is represented by a list of n strings, each of length m, containing characters '.' or '#'.
def func():
    rstr = lambda : stdin.readline().strip()
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    rint = lambda : int(stdin.readline())
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rstr_2d = lambda n: [rstr() for _ in range(n)]
    rint_2d = lambda n: [rint() for _ in range(n)]
    rints_2d = lambda n: [rints() for _ in range(n)]
    pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
    out = []
    n, m = rints()
    grid, all, ans = rstr_2d(n), [], 'YES'
    for i in range(m):
        tem = set()
        
        for j in range(n):
            if grid[j][i] == '#':
                tem.add(j)
        
        if tem:
            for j in all:
                inter = tem.intersection(j)
                if inter:
                    if inter != tem:
                        ans = 'NO'
                    break
            if tem not in all:
                all.append(tem)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 50, `m` is an integer such that 1 ≤ m ≤ 50, `grid` is a list of `n` strings, each of length `m`, containing characters '.' or '#', `all` is a list of sets, each set containing the indices of rows where the character at a specific column is '#'. If there exists any column `i` where the set of row indices `tem` intersects with any set in `all` but is not equal to that set, `ans` is 'NO'. Otherwise, `ans` remains 'YES'. If `tem` is empty for any column, it is not added to `all`. `rstr`, `rstrs`, `rint`, `rints`, `rstr_2d`, `rint_2d`, `rints_2d`, `pr` are functions/lambda functions for input/output operations, `out` is an empty list.
    print(ans)
#Overall this is what the function does:The function reads an integer grid size (n, m) and a grid of n strings, each of length m, containing characters '.' or '#'. It then processes the grid to check if any column contains a set of '#' characters that partially overlaps with any previously seen column's set of '#' characters. If such a partial overlap is found, the function outputs 'NO'. If no such partial overlap exists for any column, the function outputs 'YES'. The function also handles edge cases where columns contain no '#' characters, which are ignored in the comparison.

