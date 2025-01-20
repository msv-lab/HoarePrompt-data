#State of the program right berfore the function call: n and m are non-negative integers such that 0 <= n, m <= 1000 and there exist at least 4 different points on the grid from (0, 0) to (n, m) inclusive.
def func_1(n, m):
    if (n >= 2 and m >= 2) :
        points = [(0, 0), (n, 0), (n, m), (0, m)]
    else :
        if (n == 0) :
            points = [(0, 0), (0, m), (0, 1), (0, m - 1)]
        else :
            if (m == 0) :
                points = [(0, 0), (n, 0), (1, 0), (n - 1, 0)]
            else :
                if (n == 1) :
                    points = [(0, 0), (1, 0), (1, m), (0, m)]
                else :
                    points = [(0, 0), (0, 1), (n, 1), (n, 0)]
                #State of the program after the if-else block has been executed: `n` and `m` are non-negative integers such that 0 <= n, m <= 1000, and m != 0. There exist at least 4 different points on the grid from (0, 0) to (n, m) inclusive. If `n` is 1, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`. Otherwise, `points` is a list containing the elements [(0, 0), (0, 1), (n, 1), (n, 0)].
            #State of the program after the if-else block has been executed: `n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\), and there exist at least 4 different points on the grid from (0, 0) to (n, m) inclusive. If `m` is 0, then `points` is `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`. Otherwise, if `n` is 1, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`. If neither of these conditions is met, then `points` is `[(0, 0), (0, 1), (n, 1), (n, 0)]`.
        #State of the program after the if-else block has been executed: *`n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\). There exist at least 4 different points on the grid from (0, 0) to (n, m) inclusive. If `n` is 0, then `points` is `[(0, 0), (0, m), (0, 1), (0, m - 1)]`. If `m` is 0, then `points` is `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`. If `n` is 1, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`. Otherwise, `points` is `[(0, 0), (0, 1), (n, 1), (n, 0)]`.
    #State of the program after the if-else block has been executed: `n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\). There exist at least 4 different points on the grid from (0, 0) to (n, m) inclusive. If both `n` and `m` are at least 2, `points` is a list containing the elements [(0, 0), (n, 0), (n, m), (0, m)]. Otherwise, if `n` is 0, `points` is `[(0, 0), (0, m), (0, 1), (0, m - 1)]`. If `m` is 0, `points` is `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`. If `n` is 1, `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`.
    return points
    #`points` is a list containing the elements based on the conditions: if both n and m are at least 2, then `points` is `[(0, 0), (n, 0), (n, m), (0, m)]`. If n is 0, then `points` is `[(0, 0), (0, m), (0, 1), (0, m - 1)]`. If m is 0, then `points` is `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`. If n is 1, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `m`, which are non-negative integers such that \(0 \leq n, m \leq 1000\). Based on the values of `n` and `m`, it returns a list of points that satisfy the condition of having at least 4 different points on the grid from (0, 0) to (n, m) inclusive. Specifically:
- If both `n` and `m` are at least 2, the function returns `[(0, 0), (n, 0), (n, m), (0, m)]`.
- If `n` is 0, the function returns `[(0, 0), (0, m), (0, 1), (0, m - 1)]`.
- If `m` is 0, the function returns `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`.
- If `n` is 1, the function returns `[(0, 0), (1, 0), (1, m), (0, m)]`.

The function ensures that the returned list always contains exactly 4 distinct points on the grid, adhering to the given constraints.

