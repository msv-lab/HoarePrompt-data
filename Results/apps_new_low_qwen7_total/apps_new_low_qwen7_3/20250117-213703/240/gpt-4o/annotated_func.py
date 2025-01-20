#State of the program right berfore the function call: n and m are non-negative integers such that 0 <= n, m <= 1000, and the grid contains at least 4 different points.
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
                #State of the program after the if-else block has been executed: `n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\) and \(n, m \geq 2\). `points` is a list containing four distinct points. If `n == 1`, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`. Otherwise, `points` is `[(0, 0), (0, 1), (n, 1), (n, 0)]`
            #State of the program after the if-else block has been executed: `n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\) and \(n, m \geq 2\). `points` is a list containing four distinct points. If `m == 0`, then `points` is `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`. Otherwise, if `n == 1`, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`. Otherwise, `points` is `[(0, 0), (0, 1), (n, 1), (n, 0)]`.
        #State of the program after the if-else block has been executed: *`n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\), and the grid contains at least 4 different points. If `n == 0`, then `points` is `[(0, 0), (0, m), (0, 1), (0, m - 1)]`. If \(n \geq 2\) and \(m \geq 2\), then `points` is a list containing four distinct points: 
        #- If `m == 0`, then `points` is `[(0, 0), (n, 0), (1, 0), (n - 1, 0)]`.
        #- If `n == 1`, then `points` is `[(0, 0), (1, 0), (1, m), (0, m)]`.
        #- Otherwise, `points` is `[(0, 0), (0, 1), (n, 1), (n, 0)]`.
    #State of the program after the if-else block has been executed: `n` and `m` are non-negative integers such that \(0 \leq n, m \leq 1000\), and the grid contains at least 4 different points. After executing the if-else block, the `points` list will be defined as follows:
    #- If `n >= 2` and `m >= 2`, then `points` is a list containing the elements \[(0, 0), (n, 0), (n, m), (0, m)\].
    #- If `n == 0`, then `points` is \[(0, 0), (0, m), (0, 1), (0, m - 1)].
    #- If `m == 0` and `n >= 2`, then `points` is \[(0, 0), (n, 0), (1, 0), (n - 1, 0)].
    #- If `n == 1`, then `points` is \[(0, 0), (1, 0), (1, m), (0, m)].
    #- Otherwise, `points` is \[(0, 0), (0, 1), (n, 1), (n, 0)]
    return points
    #The program returns a list of points based on the conditions:
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `m`, which are non-negative integers such that \(0 \leq n, m \leq 1000\). It returns a list of four distinct points based on the values of `n` and `m`. The function handles various edge cases:
- If both `n` and `m` are at least 2, it returns the points \[(0, 0), (n, 0), (n, m), (0, m)\].
- If `n` is 0, it returns \[(0, 0), (0, m), (0, 1), (0, m - 1)].
- If `m` is 0 and `n` is at least 2, it returns \[(0, 0), (n, 0), (1, 0), (n - 1, 0)].
- If `n` is 1, it returns \[(0, 0), (1, 0), (1, m), (0, m)].
- Otherwise, it returns \[(0, 0), (0, 1), (n, 1), (n, 0)].

The function ensures that the grid contains at least 4 different points and the returned list always consists of four distinct points.

