#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200 000, and each of the following n lines contains two integers xi and yi such that |xi|, |yi| ≤ 109.
def func():
    n = int(raw_input())
    rows = {}
    cols = {}
    posi = {}
    for i in range(n):
        x, y = [int(t) for t in raw_input().split(' ')]
        
        if x in rows:
            rows[x] += 1
        else:
            rows[x] = 1
        
        if y in cols:
            cols[y] += 1
        else:
            cols[y] = 1
        
        if (x, y) in posi:
            posi[x, y] += 1
        else:
            posi[x, y] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `i` is `n`, `x` is the last integer input, `y` is the last integer input. If `(x, y)` is in `posi`, then `posi[(x, y)]` is the count of occurrences of `(x, y)`. Otherwise, `rows[x]` is the count of occurrences of `x` and `cols[y]` is the count of occurrences of `y`, and `posi[(x, y)]` is 1.
    ans = 0
    for t in rows.keys():
        ans = ans + (rows[t] - 1) * rows[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the sum of \((rows[t] - 1) * rows[t] / 2\) for all keys \( t \) in `rows`, and `rows` remains unchanged from its original state.
    for t in cols.keys():
        ans = ans + (cols[t] - 1) * cols[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the sum of \((rows[t] - 1) * rows[t] / 2\) for all keys \( t \) in `rows` plus \((cols[t] - 1) * cols[t] / 2\) for all keys \( t \) in `cols`, and `rows` remains unchanged from its original state.
    for t in posi.keys():
        if posi[t] > 1:
            ans -= (posi[t] - 1) * posi[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the initial value of `ans` minus the sum of \((posi[t] - 1) * posi[t] / 2\) for all keys \( t \) in `posi` such that `posi[t] > 1`, `rows` remains unchanged from its original state, and `cols` remains unchanged from its original state.
    print(ans)
#Overall this is what the function does:The function processes \(n\) pairs of integers \((x_i, y_i)\) where \(n\) is an integer such that \(1 \leq n \leq 200,000\) and each pair satisfies \(|x_i|, |y_i| \leq 10^9\). It counts the occurrences of each \(x_i\) and \(y_i\) separately and together. Specifically, it calculates the number of unique \(x_i\) values, the number of unique \(y_i\) values, and the number of pairs \((x_i, y_i)\) that occur more than once. The function then computes a result based on these counts using the formula \((count - 1) * count / 2\) for both unique \(x_i\) and \(y_i\) values and subtracts the contribution of pairs that occur more than once. Finally, it prints the computed result. Potential edge cases include the minimum and maximum values of \(n\) and the range of \(x_i\) and \(y_i\), which are handled within the given constraints.

