#State of the program right berfore the function call: H and W are integers such that 3 ≤ H, W ≤ 500. The matrix a is a H × W grid where each element is either `#` or `.`. Additionally, the first and last rows, and the first and last columns of the grid are all `.`. There is at least one `#` in the grid.
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
        
    #State of the program after the  for loop has been executed: `H` is an integer such that \(3 \leq H \leq 500\); `W` is an integer such that \(3 \leq W \leq 500\); `a` is an \(H \times W\) grid where each element is either `#` or `.`, and the first and last rows, and the first and last columns of the grid are all `.`; `n` is a positive integer less than or equal to the number of rows in the grid; `red` is a list of strings where each string represents a transformed row based on the original row according to the rules described in the loop; `blue` is a list of strings where each string represents a transformed row based on the original row according to the rules described in the loop; `row` is a string representing the input from `raw_input()` for each iteration; `r` is a list of length `m` with alternating characters `#` and `.`, starting with `#`; `b` is a list of the same length with alternating characters `.` and `#`, starting with `.`; the end of `b` has an additional `#`.
    for r in red:
        print(r)
        
    #State of the program after the  for loop has been executed: `red` must be a list containing all the transformed rows, and the code will print each transformed row stored in `red`.
    for b in blue:
        print(b)
        
    #State of the program after the  for loop has been executed: `blue` is a list, and the output of the program is the sequence of elements in `blue`.
#Overall this is what the function does:The function takes an \(H \times W\) grid represented by a matrix `a` where each element is either `#` or `.`. It also ensures that the first and last rows, and the first and last columns of the grid are all `.`. The function then creates two new grids, `red` and `blue`, where each row in these grids is transformed based on the original row. Specifically, for even-indexed rows, both `red` and `blue` have alternating `#` and `.` starting with `#` for `red` and `.` for `blue`. For odd-indexed rows, `red` and `blue` have alternating `#` and `.` starting with `#` for `red` and `.` for `blue`. If a row contains a `#`, both `red` and `blue` for that row are filled with `#`. After transformation, the function prints each row of `red` followed by each row of `blue`. This means the output consists of two sets of transformed rows, one set for `red` and one set for `blue`.

