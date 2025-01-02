#State of the program right berfore the function call: n, m, and d are integers such that 1 ≤ n, m, d ≤ 1000, and m ≤ n. The list c is a list of integers representing the lengths of the platforms, where 1 ≤ c_i ≤ n and the sum of all c_i is less than or equal to n.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m, d = rints()
    c, ans = rints(), [0] * n
    pos, su = [], 0
    for i in range(m - 1, -1, -1):
        pos.append(n + 1 - su - c[i])
        
        su += c[i]
        
    #State of the program after the  for loop has been executed: `m` must be greater than or equal to 1; `pos` is a list of length `m`, where each element is `n + 1 - su - c[j]` for `j` from `0` to `m-1`; `su` is the sum of all elements in `c` list; `n` and `c` remain unchanged.
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
        
    #State of the program after the  for loop has been executed: `m` is a positive integer, `pos` is a list of length `m + 1` where the first element is `0` and the rest of the elements are determined by the loop logic, `su` is the sum of all elements in the list `c`, `n` and `c` remain unchanged, `ans[j - 1]` for all `j` such that `pos[i] <= j < pos[i + 1]` for all valid `i` will be set to `i + 1`, `i` is `m - 1`.
    if (n + 1 - (pos[-1] + c[-1] - 1) > d) :
        print('NO')
    else :
        print('YES')
        print(' '.join(map(str, ans)))
    #State of the program after the if-else block has been executed: *`m` is a positive integer, `pos` is a list of length `m + 1` where the first element is `0` and the rest of the elements are determined by the loop logic, `su` is the sum of all elements in the list `c`, `n` and `c` remain unchanged, `ans[j - 1]` for all `j` such that `pos[i] <= j < pos[i + 1]` for all valid `i` will be set to `i + 1`, and the program prints either 'YES' or 'NO' based on whether the condition `n + 1 - (pos[-1] + c[-1] - 1) > d` is satisfied.
#Overall this is what the function does:- The function correctly handles the case where the sum of all elements in `c` is less than or equal to `n` and ensures that the distance between consecutive platforms does not exceed `d`.
- However, the function does not explicitly handle cases where the sum of elements in `c` is exactly `n` and the last platform placement results in the exact boundary condition (`n + 1 - (pos[-1] + c[-1] - 1) == d`). In such a scenario, the function should still print 'YES'.
- The function also does not handle cases where `c` contains zeros. If `c` contains a zero, it means there is no platform, and the function should handle this edge case appropriately by printing 'NO'.

