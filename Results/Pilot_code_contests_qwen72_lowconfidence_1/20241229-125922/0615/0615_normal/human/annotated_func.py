#State of the program right berfore the function call: The input consists of an integer n (2 ≤ n ≤ 10) followed by 4n + 1 lines, each containing two integers x_i, y_i (0 ≤ x_i, y_i ≤ 50). It is guaranteed that there are at least n points on each side of an axis-aligned square, and all 4n + 1 points are distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rints_2d = lambda n: [rints() for _ in range(n)]
    get_col = lambda arr, i: [row[i] for row in arr]
    n = int(input()) * 4 + 1
    a, memx, memy = rints_2d(n), [float('inf'), -1], [float('inf'), -1]
    xs, ys = Counter(get_col(a, 0)), Counter(get_col(a, 1))
    for (x, y) in a:
        if xs[x] >= n - 1 >> 2:
            memx = [min(memx[0], x), max(memx[1], x)]
        
        if ys[y] >= n - 1 >> 2:
            memy = [min(memy[0], y), max(memy[1], y)]
        
    #State of the program after the  for loop has been executed: `a` is a list of `n` lists, each containing two integers read from stdin. `xs` is a `Counter` object counting the occurrences of each x-coordinate in the first column of `a`, and `ys` is a `Counter` object counting the occurrences of each y-coordinate in the second column of `a`. `memx` is `[min(x for x in xs if xs[x] >= (n - 1) >> 2), max(x for x in xs if xs[x] >= (n - 1) >> 2)]` if there exists any x-coordinate in `xs` that meets the condition `xs[x] >= (n - 1) >> 2`; otherwise, `memx` remains `[float('inf'), -1]`. Similarly, `memy` is `[min(y for y in ys if ys[y] >= (n - 1) >> 2), max(y for y in ys if ys[y] >= (n - 1) >> 2)]` if there exists any y-coordinate in `ys` that meets the condition `ys[y] >= (n - 1) >> 2`; otherwise, `memy` remains `[float('inf'), -1]`.
    for (x, y) in a:
        if not (memx[0] < x < memx[1] and y in memy or x in memx and memy[0] <= y <=
            memy[1]):
            print('%d %d' % (x, y))
            exit()
        
    #State of the program after the  for loop has been executed: `a` is a list of `n` lists, each containing two integers, where `n` is at least 1, `xs` is a `Counter` object counting the occurrences of each x-coordinate in the first column of `a`, and `ys` is a `Counter` object counting the occurrences of each y-coordinate in the second column of `a`. `memx` and `memy` are calculated as described. After all iterations of the loop, if the condition `(memx[0] < x < memx[1] and y in memy or (x in memx and memy[0] <= y <= memy[1]))` is satisfied for every pair `(x, y)` in `a`, the program completes without printing any values. If the condition is not satisfied for any pair `(x, y)` in `a`, the values of `x` and `y` for that pair are printed, and the program terminates.
#Overall this is what the function does:The function processes input consisting of an integer `n` (2 ≤ n ≤ 10) followed by 4n + 1 pairs of integer coordinates (0 ≤ x_i, y_i ≤ 50). It identifies the smallest axis-aligned square that contains at least `n` points on each of its four sides. The function then checks each point to ensure it lies within this square. If a point does not satisfy the condition, the function prints the coordinates of that point and exits immediately. If all points satisfy the condition, the function completes without printing any values. The function assumes that the input is valid and that there are at least `n` points on each side of the square. Edge cases such as invalid input or fewer than `n` points on any side of the square are not handled by the function.

