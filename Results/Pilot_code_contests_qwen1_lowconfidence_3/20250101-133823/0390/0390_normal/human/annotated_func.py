#State of the program right berfore the function call: n, m, and d are non-negative integers such that 1 ≤ n, m, d ≤ 1000, and m ≤ n. The list c is a list of positive integers where each element c_i satisfies 1 ≤ c_i ≤ n, and the sum of all elements in c is less than or equal to n.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m, d = rints()
    c, ans = rints(), [0] * n
    pos, su = [], 0
    for i in range(m - 1, -1, -1):
        pos.append(n + 1 - su - c[i])
        
        su += c[i]
        
    #State of the program after the  for loop has been executed: `c` is a list of length `n` initialized with values from `rints()`, `ans` is a list of `n` zeros, `n` is a non-negative integer between 1 and 1000, `m` is a non-negative integer between 1 and 1000 and less than or equal to `n`, `d` is a non-negative integer between 1 and 1000, `pos` contains the calculated positions based on the sum `su` and the elements in `c`, `su` equals the sum of all elements in `c`.
    pos.append(0)
    pos.reverse()
    for i in range(m):
        if pos[i + 1] - pos[i] <= d:
            for j in range(pos[i + 1], pos[i + 1] + c[i]):
                ans[j - 1] = i + 1
            continue
        
        pos[i + 1] = min(pos[i] + d, n)
        
        for j in range(pos[i + 1], pos[i + 1] + c[i]):
            ans[j - 1] = i + 1
        
        pos[i + 1] += c[i] - 1
        
    #State of the program after the  for loop has been executed: - `pos[i + 1]` is the cumulative sum of `d` and `c[i] - 1` for each `i` up to `m-1`.
    #- `ans[j - 1]` is set to `i + 1` for the range `[pos[i], pos[i + 1])` for each `i` in the range `0` to `m-1`.
    #- `ans` contains values indicating the segment assignment for each index in the range `[0, n-1]`.
    #
    #Thus, the final output state of the loop after all iterations is:
    #
    #Output State:
    if (n + 1 - (pos[-1] + c[-1] - 1) > d) :
        print('NO')
    else :
        print('YES')
        print(' '.join(map(str, ans)))
    #State of the program after the if-else block has been executed: *`pos[i + 1]` is the cumulative sum of `d` and `c[i] - 1` for each `i` up to `m-1`; `ans[j - 1]` is set to `i + 1` for the range `[pos[i], pos[i + 1])` for each `i` in the range `0` to `m-1`; `ans` contains values indicating the segment assignment for each index in the range `[0, n-1]`; if the condition `(n + 1 - (pos[-1] + c[-1] - 1) > d)` is satisfied, 'NO' is printed; otherwise, 'YES' is printed.
#Overall this is what the function does:The function `func()` accepts three non-negative integers `n`, `m`, and `d` (with constraints 1 ≤ n, m, d ≤ 1000 and m ≤ n) and a list `c` of positive integers where each element `c_i` satisfies 1 ≤ `c_i` ≤ n and the sum of all elements in `c` is less than or equal to n. It then processes these inputs to determine whether it is possible to assign segments to indices in a way that satisfies certain conditions. If it is possible, it prints "YES" followed by the segment assignments; otherwise, it prints "NO".

The function first reads `n`, `m`, and `d` from standard input and stores them in variables `n`, `m`, and `d`. It also reads the list `c` and initializes a list `ans` of length `n` filled with zeros. It calculates a list `pos` that represents the positions based on the cumulative sums of elements in `c` and `d`.

Next, it iterates over the elements in `c` and `pos` to assign segments to indices in `ans` while ensuring that the distance between consecutive segments does not exceed `d`. If the distance between two consecutive positions in `pos` is greater than or equal to `d`, it adjusts the positions and assigns segments accordingly.

Finally, it checks if the last position plus the last element in `c` minus one is within the limit defined by `d` and `n`. If the condition is met, it prints "YES" followed by the contents of `ans`; otherwise, it prints "NO".

