#State of the program right berfore the function call: H and W are integers such that 3 ≤ H, W ≤ 500, and a_{ij} is either `#` or `.`. Additionally, a_{ij} is `.` for cells where i=1, H or j=1, W, and at least one a_{ij} is `#`.
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
        
    #State of the program after the  for loop has been executed: `r` is a list of length `m` where the first element is `'#'` and the last element is `'.'`, `b` is a list of length `m` where the first two elements are `'.', '#'`, `red` is a list containing strings of length `m` (each constructed from alternating `'#'` and `'.'` based on `i % 2`), `blue` is a list containing strings of length `m` (each constructed from alternating `'#'` and `'.'` based on `i % 2`), `i` is `n-1`, `row` is the input string from the last iteration of the loop, `j` is `m-2` if `i` is even, or `m-3` if `i` is odd.
    for r in red:
        print(r)
        
    #State of the program after the  for loop has been executed: `red` is a list of strings of length `m` containing alternating `'#'` and `'.'` based on `i % 2`, each element of `red` is printed exactly once during the loop, `i` is -1, `r` is the last element of the list `red` (which is a string of length `m` containing alternating `'#'` and `'.'` based on `i % 2`), `row` is the last printed string `r`, `j` is `m-2`.
    for b in blue:
        print(b)
        
    #State of the program after the  for loop has been executed: `blue` is a non-empty list, `red` is a list of strings of length `m` containing alternating `'#'` and `'.'` based on `i % 2`, each element of `red` is printed exactly once during the loop, `i` is the index of the last printed element in `red` (which is a string of length `m` containing alternating `'#'` and `'.'` based on `i % 2`), `r` is the last element of the list `red` (which is a string of length `m` containing alternating `'#'` and `'.'` based on `i % 2`), `row` is the last printed string `r`, `j` is `m-2`, `b` is the last printed element from the `blue` list.
#Overall this is what the function does:The function processes input dimensions \( n \) and \( m \) (where \( 3 \leq n, m \leq 500 \)), and generates two \( n \times m \) grids, one representing "red" and the other representing "blue". Each grid is filled with alternating `'#'` and `'.'` characters based on the row index \( i \) modulo 2. The function then prints each row of both grids sequentially. The red grid starts with `'#'` and ends with `'.'`, while the blue grid starts with `'.'` and ends with `'#'`. If \( i \) is even, the corresponding row in the red grid contains `'#'` followed by alternating `'#'` and `'.'`, and in the blue grid, it contains `'.'` followed by alternating `'#'` and `'#'`. If \( i \) is odd, the patterns are reversed.

