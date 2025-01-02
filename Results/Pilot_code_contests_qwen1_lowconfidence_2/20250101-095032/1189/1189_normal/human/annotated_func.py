#State of the program right berfore the function call: H and W are integers such that 3 ≤ H, W ≤ 500, and a_{ij} is either `#` or `.`. Additionally, a_{ij} is `.` if i=1, H or j=1, W, and at least one of a_{ij} is `#`.
def func():
    n, m = map(int, raw_input().split())
    red = []
    blue = []
    for i in range(n):
        row = raw_input()
        
        r = ['#']
        
        b = ['.']
        
        for j in range(1, m - 1):
            if row[j] == '#':
                r.append('#')
                b.append('#')
            elif i % 2 == 0:
                r.append('#')
                b.append('.')
            else:
                r.append('.')
                b.append('#')
        
        r.append('.')
        
        b.append('#')
        
        red.append(''.join(r))
        
        blue.append(''.join(b))
        
    #State of the program after the  for loop has been executed: `n` is the original value of `n`, `m` is the original value of `m`, `row` is a list of strings input by the user corresponding to each row of the grid, `r` is a list of length `m` where the first element is `'#'`, the last element is `'. '` and the rest of the elements alternate between `'#'` and `'.'` based on the value of `row[j]` and the parity of `j`, `b` is a list of length `m + 1` where the first and last elements are `'#'` and the rest alternate between `'#'` and `'.'`, `red` is a list of strings where each string is the joined version of the corresponding `r` list, `blue` is a list of strings where each string is the joined version of the corresponding `b` list.
    for r in red:
        print(r)
        
    #State of the program after the  for loop has been executed: `n` is the original value of `n`, `m` is the original value of `m`, `row` is a list of strings input by the user corresponding to each row of the grid, `r` is a list of strings where each string is the joined version of the corresponding `r` list and has all elements processed, `b` is a list of length `m + 1` where the first and last elements are `'#'` and the rest alternate between `'#'` and `'.'`, `red` is a list of strings where each string is the joined version of the corresponding `r` list, `blue` is a list of strings where each string is the joined version of the corresponding `b` list; all strings in `red` are printed.
    for b in blue:
        print(b)
        
    #State of the program after the  for loop has been executed: `n` is the original value of `n`, `m` is the original value of `m`, `row` is a list of strings input by the user corresponding to each row of the grid, `r` is a list of strings where each string is the joined version of the corresponding `r` list and has all elements processed, `b` is a list of length `m + 1` where the first and last elements are `'#'` and the rest alternate between `'#'` and `'.'`, `red` is a list of strings where each string is the joined version of the corresponding `r` list, `blue` is a list of strings where each string is the joined version of the corresponding `b` list, and `blue` contains all the elements of the `b` list.
#Overall this is what the function does:The function `func` accepts two parameters `H` and `W`, which represent the height and width of a grid, respectively. It processes a grid represented by `H` rows and `W` columns, where each cell can be either `#` or `.`. The function constructs two modified grids: one with alternating `#` and `.` starting from `#` (referred to as `red`), and another with alternating `#` and `.` starting from `#` but excluding the last column (referred to as `blue`). After processing, it prints both modified grids. The function does not return anything but modifies and prints the grid according to the specified patterns.

