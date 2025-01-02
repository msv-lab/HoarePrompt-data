#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, l is an integer such that 2 ≤ l ≤ 10^9, x and y are integers such that 1 ≤ x < y ≤ l, and a is a list of n integers representing the positions of the marks on the ruler, where 0 = a[0] < a[1] < ... < a[n-1] = l.
def func():
    n, l, x, y = map(int, sys.stdin.next().split())
    marks = map(int, sys.stdin.next().split())
    x_solved = False
    y_solved = False
    magic_tick = None
    for (i, mark) in enumerate(marks):
        if mark + x > l:
            break
        
        res_y = bisect.bisect_left(marks, mark + y, lo=i)
        
        res_x = bisect.bisect_left(marks, mark + x, lo=i, hi=min(res_y + 1, n))
        
        res_x = min(max(0, res_x), n - 1)
        
        res_y = min(max(0, res_y), n - 1)
        
        if marks[res_x] == mark + x:
            x_solved = True
        
        if marks[res_y] == mark + y:
            y_solved = True
        
    #State of the program after the  for loop has been executed: `n` is an integer, `l` is an integer, `x` is an integer, `y` is an integer, `a` is a list of `n` integers representing the positions of the marks on the ruler, `marks` is a map object of integers, `x_solved` is a boolean, `y_solved` is a boolean, `magic_tick` is `None`, `i` is `n` (the length of `marks`), `mark` is the last value in the `marks` map, `res_y` is `n` (the length of `marks`), `res_x` is `n` (the length of `marks`), `x_solved` is `True` if there exists any `mark` such that `marks[res_x] == mark + x`, `y_solved` is `True` if there exists any `mark` such that `marks[res_y] == mark + y`.
    if (x_solved and y_solved) :
        print(0)
    else :
        if (x_solved and not y_solved) :
            print(1)
            print(y)
        else :
            if (not x_solved and x_solved) :
                print(1)
                print(x)
            else :
                for (shift_x, shift_y) in [(x, y), (-x, y), (x, -y), (x, y)]:
                    i, j = 0, 0
                    
                    while True:
                        if i >= n or j >= n:
                            break
                        if marks[i] + shift_x > marks[j] + shift_y:
                            j += 1
                        elif marks[i] + shift_x < marks[j] + shift_y:
                            i += 1
                        elif 0 <= marks[i] + shift_x <= l:
                            magic_tick = marks[i] + shift_x
                            break
                        else:
                            i += 1
                            j += 1
                    
                #State of the program after the  for loop has been executed: `i` and `j` are integers such that `0 <= i < n` and `0 <= j < n` (with one of them being equal to `n`), `magic_tick` is set to `marks[i] + shift_x` if the condition `0 <= marks[i] + shift_x <= l` is met, `x_solved` is `True` if there exists at least one `mark` such that `marks[res_x] == mark + x`, `y_solved` remains `False` unless a valid `mark` is found for `y` in subsequent iterations, and `marks`, `shift_x`, `shift_y`, and `l` remain unchanged.
                if magic_tick :
                    print(1)
                    print(magic_tick)
                else :
                    print(2)
                    print('%i %i' % (x, y))
                #State of the program after the if-else block has been executed: *`i` and `j` are integers such that `0 <= i < n` and `0 <= j < n` (with one of them being equal to `n`). `x_solved` is `True` if there exists at least one `mark` such that `marks[res_x] == mark + x`. `y_solved` remains `False` unless a valid `mark` is found for `y` in subsequent iterations. `marks`, `shift_x`, `shift_y`, and `l` remain unchanged. Additionally, a value of `1` is printed if `magic_tick` is `True`.
            #State of the program after the if-else block has been executed: *`n` is an integer, `l` is an integer, `x` is an integer, `y` is an integer, `a` is a list of `n` integers representing the positions of the marks on the ruler, `marks` is a map object of integers, `x_solved` is a boolean, `y_solved` is a boolean, `magic_tick` is `None`, `i` is `n` (the length of `marks`), `mark` is the last value in the `marks` map, `res_y` is `n` (the length of `marks`), `res_x` is `n` (the length of `marks`), and the condition `(not x_solved and x_solved)` is evaluated as `False`. Therefore, `x_solved` is `False`, `y_solved` remains `True`, `i` and `j` are integers such that `0 <= i < n` and `0 <= j < n` (with one of them being equal to `n`). A value of `1` is printed if `magic_tick` is `True`.
        #State of the program after the if-else block has been executed: *`n` is an integer, `l` is an integer, `x` is an integer, `y` is an integer, `a` is a list of `n` integers representing the positions of the marks on the ruler, `marks` is a map object of integers, `x_solved` is a boolean, `y_solved` is a boolean, `magic_tick` is `None`, `i` is `n` (the length of `marks`), `mark` is the last value in the `marks` map, `res_y` is `n` (the length of `marks`), `res_x` is `n` (the length of `marks`). If `x_solved` is `True` and `y_solved` is `False` or no such `mark` exists, `y` is printed. Otherwise, if `x_solved` is `False` and `y_solved` is `True`, `1` is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer, `l` is an integer, `x` is an integer, `y` is an integer, `a` is a list of `n` integers representing the positions of the marks on the ruler, `marks` is a map object of integers, `x_solved` is a boolean, `y_solved` is a boolean, `magic_tick` is `None`, `i` is `n` (the length of `marks`), `mark` is the last value in the `marks` map, `res_y` is `n` (the length of `marks`), `res_x` is `n` (the length of `marks`). If both `x_solved` and `y_solved` are `True`, the console outputs `0`. Otherwise, if `x_solved` is `True` and `y_solved` is `False`, `y` is printed. If `x_solved` is `False` and `y_solved` is `True`, `1` is printed.
#Overall this is what the function does:The function `func` accepts the parameters `n` (an integer such that 2 ≤ n ≤ 10^5), `l` (an integer such that 2 ≤ l ≤ 10^9), `x` and `y` (integers such that 1 ≤ x < y ≤ l), and `a` (a list of n integers representing the positions of the marks on the ruler, where 0 = a[0] < a[1] < ... < a[n-1] = l). The function determines whether there are marks on the ruler at positions `x + a[i]` and `y + a[i]` for any `i` in the range [0, n-1]. If both marks exist, it prints `0`. If only the mark at position `x + a[i]` exists, it prints `1` and the position `y`. If only the mark at position `y + a[i]` exists, it prints `1` and the position `x`. If neither mark exists, it prints `2` and the pair `(x, y)`.

The function iterates through the list of marks and uses binary search to check if the positions `x + a[i]` and `y + a[i]` are occupied. If either of these positions is found, it sets the corresponding flags `x_solved` or `y_solved` to `True`. After the iteration, based on the states of `x_solved` and `y_solved`, it prints the appropriate output.

If neither mark is found, the function enters an additional nested loop to find a position `tick` on the ruler such that `tick + x` or `tick + y` falls within the valid range `[0, l]`. If such a position is found, it prints `1` and the position `tick`. If no valid `tick` is found, it prints `2` and the pair `(x, y)`.

In all cases, the function prints either `0`, `1` followed by a position, or `2` followed by a pair of positions. The final state of the program after the function concludes includes the values of `x_solved`, `y_solved`, and the printed output.

